from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.db import models

class User(AbstractUser):
    pass
# class UserProfile(models.Model):
#
#     user = models.OneToOneField(User)
#
#     def __unicode__(self):
#         return self.user.username

class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
