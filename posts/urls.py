from .views import BlogsList, BlogView
from django.conf.urls import url,include
from comments.views import CommentView
from core.views import test


urlpatterns = [
    url(r'^blogs/$', BlogsList.as_view(), name="allblogs"),
    url(r'^core/$', test, name="mainpage"),
    url(r'^blogs/(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^blogs/(?P<pk>\d+)/comments/$', CommentView.as_view(), name="allcomments"),
  #  url(r'^comments/(?P<pk>\d+)/comments$', BlogView.as_view(), name="allcomment"),
]
