from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^post/(?P<id>\d+)$', views.post),
    url(r'^comment/(?P<post_id>\d+)$', views.comment),
  
    url(r'^add/(?P<id>\d+)$', views.add),


]
