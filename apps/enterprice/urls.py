#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\3\7 9:24'

"""lagou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from .views import CompanyView,CommentView,CompanyListView,CompanyDetailView

app_name="enterprice"

urlpatterns = [
    re_path('detail/(?P<enterprice_id>\d+)/', CompanyDetailView.as_view(), name="company_page"),
    path('', CompanyView.as_view(), name="company_info_page"),
    path('comments/', CommentView.as_view(), name="comment_page"),
    path('list/', CompanyListView.as_view(), name="company_list_page"),
]