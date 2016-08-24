import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tut.settings')
#Add the DJANGO_SETTINGS_MODULE variables, as done by manage.py

import django
django.setup()
#Import project setting

from rango.models import Category, Page
#Define the following function to add the page and the cat
def populate():
    #Define the pages for each category. Use a list of dictionary elements
    python_pages = [{'title': 'Official python tutorial',
                     'url': 'http://docs.python.org/2/tutorial/', 'views': 432},
                    {'title': 'How to think like a computer scientist',
                     'url': 'http://www.greenteapress.com/thinkpython', 'views': 65},
                    {'title': 'Lean Python in 10 minutes',
                     'url': 'http://www.korokithakis.net/tutorials/python', 'views': 242}]

    django_pages = [{'title': 'Official Django tutorial',
                     'url': 'https://docs.djangoproject.com/en/1.9/intro/tutorial01/', 'views': 54},
                    {'title': 'Django Rocks',
                     'url': 'http://www.djangorocks.com', 'views': 17},
                    {'title': 'How to tango with django',
                     'url': 'http://www.tangowithdjango.com', 'views': 32}]
    other_pages = [{'title': 'Bottle',
                    'url': 'http://bottepy.org/docs/dev/', 'views': 25},
                   {'title': 'Flask',
                    'url': 'http://flask.pocoo.org', 'views': 575}]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 32},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}}

    #Now, add categories
    for cat_name, cat_pages in cats.items():
        print('Adding category with name: ' + cat_name)
        curcat = add_cat(cat_name,cat_pages['views'],cat_pages['likes'])
        #print('Views: {0}, Likes: {1}'.format(str(cat_pages['views']),str(cat_pages['likes'])))
        #Now add all pages for each category
        for page in cat_pages['pages']:
            add_page(curcat, page['title'], page['url'], page['views'])


    #Print all categories
    for c in Category.objects.all():
        print('Found category with name: {0}, views: {1}, likes: {2}'.format(c.name,c.views,c.likes))
        #Display all the pages asscoated with each Categories
        for p in Page.objects.filter(category=c):
            print('Page: {0}'.format(str(p)))

    pass

def add_page(cat, title, url, views):
    #Add a page
    p= Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    p.save()
    return p

def add_cat(name,views,likes):
    #Add a category
    c = Category.objects.get_or_create(name=name)[0]
    #For updating, we just get it and change the attritube
    c.views = views
    c.likes = likes
    c.save()
    return c

if  __name__=='__main__':
    #Define what happens to a standalone script python populate_rango.py
    print("Start Rango population script...")
    populate()