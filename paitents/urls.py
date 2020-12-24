# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url

from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns=[

    path('paitents/home',views.index,name='index'),

    #path('home',views.home,name='home'),
    #url(r'^register/$',views.register),

    path('paitents/register',views.register, name='register'),

    path('paitents/login', views.login, name='login'),
    #path('add',views.add, name='add')

    path('paitents/logout', views.logout, name='logout'),

    path('paitents/patientlogin',views.patientlogin,name='patientlogin'),
    path('paitents/patienthome',views.patienthome,name='patienthome'),
    path('paitents/viewrecords',views.viewrecords,name='viewrecords'),

]