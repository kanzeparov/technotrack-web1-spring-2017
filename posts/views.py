#coding: utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Blog, Post
from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from django.contrib.auth import get_user_model







class CreateUser(CreateView):
    model=get_user_model()
    template_name = 'posts/register.html'
    fields = ('title', 'description')
    success_url = 'core/login/'


class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', u'Заголовок'),
        ('rate', u'Рейтинг'),
        ('description', u'Описание'),
    ))
    search = forms.CharField(required=False)


class Categories(models.Model):
    title = forms.CharField(max_length=30)

class UpdateBlog(UpdateView):

    template_name = 'posts/editblog.html'
    model = Blog
    fields = ('title', 'description', 'categories')
    success_url = '/blogs/'
    categories = models.ManyToManyField(Categories)

    def get_queryset(self):
        return super(UpdateBlog, self).get_queryset().filter(author=self.request.user)


class UpdatePost(UpdateView):

    template_name = 'posts/editpost.html'
    model = Post
    fields = ('title', 'description', 'blog')
    success_url = '/blogs/'

    def get_queryset(self):
        return super(UpdatePost, self).get_queryset().filter(author=self.request.user)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','description','rate')



class CreateBlog(CreateView):
    categories = models.ManyToManyField(Categories)
    template_name = 'posts/addblog.html'
    model = Blog
    fields = ('title', 'description','categories')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreateBlog, self).form_valid(form)


class CreatePost(CreateView):
    template_name = 'posts/addpost.html'
    model = Post
    model1 = Blog
    fields = ('title', 'description', 'blog')
    success_url = '/blogs/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.rate = 0
        return super(CreatePost, self).form_valid(form)


class BlogsList(ListView):
    queryset = Blog.objects.all()
    template_name = 'posts/blogs.html'
    sortform = None


    def dispatch(self, request, *args, **kwargs):
        self.sortform = SortForm(self.request.GET)
        return super(BlogsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogsList, self).get_context_data(**kwargs)
        context['sortform'] = SortForm()
        return context

    def get_queryset(self):
        qs = super(BlogsList, self).get_queryset()
        if self.sortform.is_valid():
            qs = qs.order_by(self.sortform.cleaned_data['sort'])
            if self.sortform.cleaned_data['search']:
                qs = qs.filter(title__icontains=self.sortform.cleaned_data['search'])
        return qs


class BlogView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'posts/blog.html'


class PostView(DetailView):
    queryset = Blog.objects.all()
    template_name = 'posts/post.html'
