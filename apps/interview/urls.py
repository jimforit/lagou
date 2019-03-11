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
from .views import MyInterviewView,InterviewCommentView,InterviewDetailView,InterviewRecordView,InterviewResultView,InterviewView,InvitationView

app_name="interview"

urlpatterns = [
    path('mine/', MyInterviewView.as_view(), name="myinterview_page"),
    re_path('(?P<resume_id>\d+)/', InterviewView.as_view(), name="interview_page"),
    path('invitations/', InvitationView.as_view(), name="invitation_page"),
    path('record/', InterviewRecordView.as_view(), name="interview_record_page"),
    path('detail/', InterviewDetailView.as_view(), name="interview_detail_page"),
    re_path('result/(?P<interview_id>\d+)', InterviewResultView.as_view(), name="interview_result_page"),
    path('comment/', InterviewCommentView.as_view(), name="interview_comment_page"),
]