from django.contrib import admin

# Register your models here.

from models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    #Display the following in the admin page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    #Generate the slug field from the name field when typing. Not save

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)