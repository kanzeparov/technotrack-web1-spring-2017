from .views import BlogsList, BlogView, CreateBlog, UpdateBlog, CreatePost, UpdatePost, CreateCategory
from django.conf.urls import url,include
from comments.views import CommentView
from django.contrib.auth.decorators import login_required
from core.views import HomePageView
from views import PostView


urlpatterns = [
    url(r'^$', BlogsList.as_view(), name="allblogs"),
    url(r'^new/$', login_required(CreateBlog.as_view()), name="createblog"),
    url(r'^category/$', CreateCategory.as_view(), name="createcategory"),
    url(r'^posts/new$', login_required(CreatePost.as_view()), name="createpost"),
    url(r'^(?P<pk>\d+)/edit/$', UpdateBlog.as_view(), name="editblog"),
    url(r'^(?P<pk>\d+)/edit/post/$', UpdatePost.as_view(), name="editpost"),
    url(r'^(?P<pk>\d+)/$', BlogView.as_view(), name="oneblog"),
    url(r'^posts/(?P<pk>\d+)$', CommentView.as_view(), name="postview"),
    url(r'^/?sort=title&search=(?P<pk1>\d+)$', CommentView.as_view(), name="myblogs"),
    url(r'^$', CommentView.as_view(), name='createcomment'),
  #  url(r'^comments/(?P<pk>\d+)/comments$', BlogView.as_view(), name="allcomment"),
]
