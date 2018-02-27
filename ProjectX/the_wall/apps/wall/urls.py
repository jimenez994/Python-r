from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^post$', views.post),
    url(r'^comment/(?P<post_id>\d+)$', views.comment),
    
    
    
]

