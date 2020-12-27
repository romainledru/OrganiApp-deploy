from django.contrib import admin
from django.urls import path, include, re_path
#from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.entryView, name='entry'),
    path('index/', views.indexView, name='index'),
    re_path(r'^index/(?P<list_id>[0-9]+)/$', views.detailView, name='detail'),
]
