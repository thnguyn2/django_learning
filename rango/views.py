from django.shortcuts import render
#This method is used to update the template with the dict

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from rango.models import Category, Page
from rango.forms import CategoryForm

def index(request):
    #First, get 5 categories after sorting in descending order
    all_cats = Category.objects.order_by('-likes')[:5]
    most_views_pages = Page.objects.order_by('-views')[:5]
    #Extract 5 most view category and send it to the context, '-' is the minus sign since the order_by will sort by increasing order
    context_dict = {'categories': all_cats, 'most_view_pages': most_views_pages}
    #'categories' is the name of the context variable

    #update_content = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!!!'}
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request,category_name_slug):
    context_dict ={}
    #Dictionary for rendering the page
    try:
        #Get the current category
        cur_cat = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=cur_cat)
        context_dict['pages'] = pages
        context_dict['category'] = cur_cat

    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context=context_dict)

def index2(request):
    return HttpResponse("Hello, this is the second response from the Rango view.")

def about(request):
    about_content = {'your_name': 'Tan Huu Nguyen'}
    return render(request, 'rango/about.html', context=about_content)

def add_category(request):
    form = CategoryForm()
    #Create a new form
    if request.method=='POST':
        #if this is an HTTP post
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            #cat is an instance of the saved category
            print(cat, cat.slug)
            return index(request)
        else:
            #Print the error to the terminal
            print(form.errors)
    #Handle the bad form, no form or new form
    return render(request, 'rango/add_category.html', {'form': form})


