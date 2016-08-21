from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the first response from the Rango view. See the about page <a href='/rango/about'>About</a>")

def index2(request):
    return HttpResponse("Hello, this is the second response from the Rango view.")

def about(request):
    return HttpResponse("Rango says here is the about page. Go back to the <a href='/'>main</a> page. Otherwise, go to the <a href='/rango/''>second</a> page")
