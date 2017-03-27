from __future__ import unicode_literals

from django.db import models
from application import settings

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    def __unicode__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    rate = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey(Blog)
    rate = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)


