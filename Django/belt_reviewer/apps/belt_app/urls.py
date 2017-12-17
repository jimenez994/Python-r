from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^register$',views.register),
    url(r'^login$', views.login),
    url(r'^wall$', views.wall),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^newbook$', views.newbook),
    url(r'^add$', views.add),

]
