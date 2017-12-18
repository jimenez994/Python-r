from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^friends$', views.friends),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^user/(?P<id>\d+)/friend$', views.add),
    url(r'^user/(?P<id>\d+)/unfriend$', views.remove),

]
