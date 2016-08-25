from django.conf.urls import url
#This
import views

urlpatterns = [
    url(r'^$', views.index2, name='index 2 function'),
    url(r'^about/$', views.about, name='about function'),
    url(r'^add_category/$',views.add_category,name='add_category'),
    url(r'category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show category'),
    #<category_name_slug> is a variable name, allows us to extract the value later on, [\w\-]+ is any alphanumeric sequence
]