from django.shortcuts import render,redirect
from django.views import View
from user.models import User
from .models import Resume
from db.login_mixin import LoginRequiredMixin
from django.urls import reverse
from delivery.models import Delivery

# Create your views here.
class ResumDetailView(LoginRequiredMixin,View):
    '''微简历'''
    def get(self,request,resume_id):
        resume = Resume.objects.get(id=resume_id)
        resume.speciality=resume.speciality.split("/")
        delivery = Delivery.objects.filter(resume_id=resume_id,delivery_status="DD",enterprice=request.user.enterprice_set.all()[0]).first()

        return render(request, 'resume_detail.html',{"resume_data":resume,"delivery":delivery})

class ResumeListView(LoginRequiredMixin,View):
    '''简历列表'''
    def get(self,request):
        resume_list = Resume.objects.filter(is_public=0)
        return render(request, 'resumelist.html',{"resume_list":resume_list})


class ResumeView(LoginRequiredMixin,View):
    '''我的简历'''
    def get(self,request):
        resume = Resume.objects.filter(email=request.user.email).first()
        user = User.objects.filter(email=request.user.email)
        if resume:
            resume.speciality = resume.speciality.split("/")
            return render(request,"resume_detail.html",{"resume_data":resume,"user":user})
        else:
            return render(request, 'resume.html')

    def post(self,request):
        resume = Resume()
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
        user = User.objects.filter(email=request.user.email).first()
        resume.user_id = user.id
        resume.save()

        user.gender = resume.gender
        user.mobile = resume.mobile
        user.nick_name = '拉勾用户'+resume.mobile[-4:]
        user.image = "/static/images/"+request.POST.get("self_image","")
        user.save()
        message = "简历更新成功,快去投简历吧"
        return render(request, 'successful.html',{"message":message})


class ResumeCollectionView(LoginRequiredMixin,View):
    '''简历收藏列表'''
    def get(self,request):

        return render(request, 'resume_collections.html')