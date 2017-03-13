from django.views.generic.base import TemplateView
from django.shortcuts import render
from posts.models import Post, Blog
from comments.models import Comment

def test(request):

    return render(request, 'core/home.html',{"count_blog": Blog.objects.all().count(),"count_post":Post.objects.all().count(), "count_comments":Comment.objects.all().count()})