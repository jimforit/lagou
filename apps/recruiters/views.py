#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\21 21:21'

from django.shortcuts import render
from django.views import View
from .forms import RegisterForm
from .models import *


class InterviewRecordView(View):
    '''面试邀请'''
    def get(self,request):
        return render(request, 'interviews_record.html')



class InterviewResultView(View):
    '''面试结果'''
    def get(self,request):
        return render(request, 'interview_result.html')

class InterviewDetailView(View):
    '''面试详情页面'''
    def get(self,request):
        return render(request, 'interview_detail.html')

class InterviewCommentView(View):
    '''面试评价'''
    def get(self,request):
        return render(request, 'interview_comment.html')

class CommentView(View):
    '''公司评价页'''
    def get(self,request):
        return render(request, 'comment.html')

class ResumeCollectionView(View):
    '''简历收藏列表'''
    def get(self,request):
        return render(request, 'resume_collections.html')




class DeliveryRecuiterView(View):
    '''招聘者页面'''
    def get(self,request):
        return render(request, 'deliveries_recruiter.html')

class RecuiterView(View):
    '''招聘需求页面'''
    def get(self,request):
        return render(request, 'recruiter.html')

class OfferView(View):
    '''Offer提交页面'''
    def get(self,request):
        return render(request, 'offer.html')

class OfferDetailView(View):
    '''招聘需求页面'''
    def get(self,request):
        return render(request, 'offer_detail.html')

