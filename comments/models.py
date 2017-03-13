from __future__ import unicode_literals

from django.db import models
from application import settings
from posts.models import Blog,Post
# Create your models here.
class Comment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    rate = models.IntegerField