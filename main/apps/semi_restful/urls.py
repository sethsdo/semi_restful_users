from django.conf.urls import url
from . import views 
  
urlpatterns = [
    url(r'^$', views.user_table),
    url(r'^new$', views.index),
    url(r'^create$', views.new),
    url(r'^show/(?P<num>\d+)$', views.user_info),
    url(r'^edit/(?P<num>\d+)$', views.edit_info),
    url(r'^id/(?P<num>\d+)$', views.edit),
    url(r'^delete/(?P<num>\d+)$', views.delete),
]
