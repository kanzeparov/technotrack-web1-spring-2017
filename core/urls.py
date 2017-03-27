from django.conf.urls import url
from views import HomePageView
from .views import RegisterFormView
from  django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^login/$', login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^register/$', RegisterFormView.as_view(), name='register'),
]