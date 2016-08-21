"""django_tut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from rango import views
from django.conf.urls import url
#Import the url objects to define the mapping
from django.contrib import admin
from django.conf.urls import include
#This is a method to h
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index1'),
    url(r'^rango/',include('rango.urls')),
    #The remainder of the string after stripping rango will be handled by rango.url.
    # Here, we import other URL configuration module. Not ending with $ but a /
    #reg, views. kwargs, name = None, prefix=''
]
