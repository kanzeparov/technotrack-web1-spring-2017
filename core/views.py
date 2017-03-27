from django.views.generic.base import TemplateView
from django.shortcuts import render
from posts.models import Post, Blog
from comments.models import Comment
from django import forms
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from models import UserRegistration

class HomePageView(TemplateView):

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['blog_count'] = Blog.objects.all().count()
        context['post_count'] = Post.objects.all().count()
        context['comment_count'] = Comment.objects.all().count()
        return context

class RegisterFormView(FormView):
    form_class = UserRegistration
    success_url = "/"
    template_name = "core/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

