from django.conf.urls import url
#This
import views
app_name = 'rango'

urlpatterns = [
    url(r'^$', views.index2, name='rango_main'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    #<category_name_slug> is a variable name, allows us to extract the value later on, [\w\-]+ is any alphanumeric sequence
]