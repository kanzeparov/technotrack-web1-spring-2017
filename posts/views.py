from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Blog, Post

class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'

class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'
