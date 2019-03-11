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
from .views import ResumDetailView,ResumeListView,ResumeCollectionView,ResumeView

app_name = 'resume'

urlpatterns = [
    path('', ResumeView.as_view(), name="resume_page"),
    re_path('detail/(?P<resume_id>\d+)/', ResumDetailView.as_view(), name="resume_detail_page"),
    path('list/', ResumeListView.as_view(), name="resume_list_page"),
    path('collection/', ResumeCollectionView.as_view(), name="resume_collection_page"),
]