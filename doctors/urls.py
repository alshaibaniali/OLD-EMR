# -*- coding: utf-8 -*-

from django.urls import path
from django.conf.urls import url

from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[

    path('doctors/home',views.index,name='index'),

    #path('home',views.home,name='home'),
    #url(r'^register/$',views.register),

    path('doctors/doc_register',views.doc_register, name='doc_register'),

    path('doctors/login', views.login, name='login'),
    #path('add',views.add, name='add')

    path('doctors/logout', views.logout, name='logout'),

    path('doctors/moduleContains', views.moduleContains, name='moduleContains'),

    path('doctors/copd', views.copd, name='copd'),

    path('copdresults', views.copdresults, name='copdresults'),

    path('doctors/diabetes', views.diabetes, name='diabetes'),

    path('diabetesresults', views.diabetesresults, name='diabetesresults'),

    path('doctors/heart', views.heart, name='heart'),

    path('heartresults', views.heartresults, name='heartresults'),

    path('doctors/lung', views.lung, name='lung'),

    path('lungresults', views.lungresults, name='lungresults'),

    path('doctors/accountUpdate',views.accountUpdate,name='accountUpdate'),

]

urlpatterns += staticfiles_urlpatterns()