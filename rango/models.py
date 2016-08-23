from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
    #Define a list of fields
    name = models.CharField(max_length=128, unique=True)
    #Make the field unique

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    #Many Pages can be linked to one Category
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title




