from django.shortcuts import render
#This method is used to update the template with the dict

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    update_content = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!!!'}
    return render(request, 'rango/index.html', context=update_content)

def index2(request):
    return HttpResponse("Hello, this is the second response from the Rango view.")

def about(request):
    return HttpResponse("Rango says here is the about page. Go back to the <a href='/'>main</a> page. Otherwise, go to the <a href='/rango/''>second</a> page")
