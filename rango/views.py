from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, this is the first response from the Rango view.")

def index2(request):
    return HttpResponse("Hello, this is the second response from the Rango view.")