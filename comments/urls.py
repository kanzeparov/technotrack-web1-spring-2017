from posts.views import BlogsList, BlogView
from .views import CommentView
from django.conf.urls import url,include


urlpatterns = [
    url(r'^$', CommentView.as_view(), name='createcomment'),
]