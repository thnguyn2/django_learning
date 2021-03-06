from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):
    #Define a list of fields
    name = models.CharField(max_length=128, unique=True)
    #Make the field unique
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    #A short label containing labels, characters, hyphen and underscore
    #blank = True allows blankspace


    class Meta:
        verbose_name_plural = 'categories'
        #Define how the plural should be, it is just a meta option, define everything but not a field

    def __str__(self):
        return self.name


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        # Super will give the base class of Category (the derived class)


class Page(models.Model):
    category = models.ForeignKey(Category)
    #Many Pages can be linked to one Category
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title




