from .views import BlogsList, BlogView
from django.conf.urls import url,include
from comments.views import CommentView
from core.views import HomePageView
from views import PostView


urlpatterns = [
    url(r'^$', BlogsList.as_view(), name="allblogs"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^posts/(?P<pk>\d+)$', CommentView.as_view(), name="postview"),
  #  url(r'^comments/(?P<pk>\d+)/comments$', BlogView.as_view(), name="allcomment"),
]
