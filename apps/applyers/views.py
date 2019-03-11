#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\25 17:34'

from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegisterForm,LoginForm
from .models import User,Resumer

class LoginView(View):
    '''用户登录'''
    def get(self,request):
        email = request.session.get("email",None)
        password = request.session.get("password",None)
        if request.session.get("email",None) and request.session.get("password",None):
            user = User.objects.filter(email=email,password=password).first()
            return render(request,"profile.html",{"user":user})
        return render(request, 'login.html')

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.filter(email__exact=email, password__exact=password).first()
            if user.nick_name:
                request.session["email"]=user.email
                request.session["password"]=user.password
                request.session["role_id"]=user.role_id
                request.session["nickname"] = user.nick_name
                return render(request, 'profile.html',{"user":user})
            elif not user.nick_name:
                request.session["email"]=user.email
                request.session["password"]=user.password
                return render(request, 'resume.html')
            else:
                return render(request, 'login.html', {'message': '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': form})


class RegisterView(View):
    '''用户注册'''
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=request.POST.get('email', ''))
            if user:
                message="邮箱已经注册"
                return render(request, 'register.html', {'message': message})
            else:
                new_user = User()
                new_user.email = form.cleaned_data["email"]
                new_user.password = form.cleaned_data["password"]
                new_user.role_id=1
                new_user.save()
        else:
            msg ={}
            if "email" in form.errors.keys():
                msg={"message1":"请输入有效的电邮地址"}
            if "password" in form.errors.keys():
                msg.update({"message2":"密码不能为空"})
            print(msg)
            return render(request, 'register.html', {'register_form': msg})
        return render(request, 'login.html', {'message': "注册成功，请登录"})

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {"form": form})

class MyInterviewView(View):
    '''面试邀请'''
    def get(self,request):
        return render(request, 'my_interviews.html')

class InterviewView(View):
    '''面试邀请函'''
    def get(self,request):
        return render(request, 'interview.html')

class InvitationView(View):
    '''邀约'''
    def get(self,request):
        return render(request, 'invitation.html')

class PofileView(View):
    '''个人信息'''
    def get(self,request):
        return render(request, 'profile.html')

class ResumeListView(View):
    '''简历列表'''
    def get(self,request):
        return render(request, 'resumelist.html')

class CompanyView(View):
    '''公司详情介绍页'''
    def get(self,request):
        return render(request, 'company.html')

class CompanyListView(View):
    '''公司列表页'''
    def get(self,request):
        return render(request, 'companylist.html')

class JobCustomizeView(View):
    '''岗位订阅'''
    def get(self,request):
        return render(request, 'job_customize.html')

class JobListView(View):
    '''岗位列表'''
    def get(self,request):
        return render(request, 'index.html')

class ResumView(View):
    '''我的简历'''
    def get(self,request):
        resumer = Resumer.objects.filter(email=request.session.get("email","")).first()
        user = User.objects.filter(email=resumer.email)
        if resumer:
            return render(request,"resume_detail.html",{"resumer_data":resumer,"user":user})
        else:
            return render(request, 'resume.html')

    def post(self,request):
        resume = Resumer()
        resume.name = request.POST.get("name","")
        resume.creer_time = request.POST.get("creer_time","")
        resume.age = request.POST.get("age", "")
        resume.self_desc = request.POST.get("self_desc", "")
        resume.mobile = request.POST.get("mobile", "")
        resume.email = request.POST.get("email","")
        resume.school = request.POST.get("school", "")
        resume.major = request.POST.get("major", "")
        resume.lastest_job_desc = request.POST.get("lastest_job_desc", "")
        resume.lastest_job_position = request.POST.get("lastest_job_position", "")
        resume.desire_position = request.POST.get("desire_position","")
        resume.desire_monthly_salary = request.POST.get("desire_monthly_salary", "")
        resume.desire_city = request.POST.get("desire_city", "")
        resume.gender = request.POST.get("gender", "")
        resume.speciality = request.POST.get("speciality", "")
        user = User.objects.filter(email=request.session.get("email","")).first()
        resume.user_id = user.id
        resume.save()

        user.gender = resume.gender
        user.mobile = resume.mobile
        user.nick_name = '拉勾用户'+resume.mobile[-4:]
        user.image = "/static/images/"+request.POST.get("self_image","")
        user.save()
        message = "简历更新成功"
        return render(request, 'resume_detail.html',{"resume_form":resume,"message":message})

class JobView(View):
    '''工作详情页'''
    def get(self,request):
        return render(request, 'job.html')

class ResumDetailView(View):
    '''微简历'''
    def get(self,request):
        return render(request, 'resume_detail.html')

class PositionView(View):
    '''岗位信息'''
    def get(self,request):
        return render(request, 'search.html')

class CollectionView(View):
    '''收藏列表'''
    def get(self,request):
        return render(request, 'collections.html')

class DeliveryView(View):
    '''投递列表'''
    def get(self,request):
        return render(request, 'deliveries.html')

class UserView(View):
    '''用户登录'''
    def get(self,request):
        return render(request, 'profile.html')

    def post(self,request):
        return render(request,'register.html')

class LagouView(View):
    '''用户登录'''
    def get(self,request):
        return render(request, 'lagou.html')

class LogoutView(View):
    '''用户登录'''
    def get(self,request):
        request.session.clear()
        return render(request, 'login.html')