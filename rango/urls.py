from django.conf.urls import url
#This
import views

urlpatterns = [
    url(r'^$', views.index2, name='index 2 function'),
    url(r'^about/$', views.about, name='about function'),
]