
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.rooms),
    url(r'^create/$', views.create),
    url(r'^system_message/$', views.system_message),
    url(r'^(?P<slug>.*)$', views.room),
]
