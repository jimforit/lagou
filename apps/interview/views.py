from django.shortcuts import render,redirect,reverse
from django.views import View
from db.login_mixin import LoginRequiredMixin
from resume.models import Resume
from interview.models import Interview
from job.models import Position
# Create your views here.
class MyInterviewView(LoginRequiredMixin,View):
    '''面试邀请'''
    def get(self,request):
        interview_ym_list = Interview.objects.filter(interview_status="YM",user=request.user)
        interview_jm_list = Interview.objects.filter(interview_status="JM", user=request.user)
        return render(request, 'my_interviews.html',{"interview_ym_list":interview_ym_list,"interview_jm_list":interview_jm_list})

class InterviewView(LoginRequiredMixin,View):
    '''面试邀请函'''
    def get(self,request,resume_id):
        resume = Resume.objects.get(id=resume_id)
        position_list = Position.objects.filter(enterprice_id=request.user.enterprice_set.all()[0].id)
        return render(request, 'interview.html',{"resume":resume,"position_list":position_list})


class InvitationView(LoginRequiredMixin,View):
    '''邀约'''
    def get(self,request):
        if request.user.role.name == "recruiter":
            return render(request, 'profile.html')
        else:
            resume = Resume.objects.get(user_id=request.user.id)
            if resume.is_public == 0:
                block = "block"
                none = "none"
                class_name = "plus open"
            else:
                block = "none"
                none = "block"
                class_name = "plus"
            return render(request, 'invitation.html',{"block":block,"none":none,"class_name":class_name})


class InterviewRecordView(LoginRequiredMixin,View):
    '''面试邀请'''
    def get(self,request):
        interview_jm_list = Interview.objects.filter(interview_status="JM",enterprice=request.user.enterprice_set.all()[0])
        resume_list = []
        for applier in  interview_jm_list:
            resume = applier.user.resume_set.all()[0]
            resume_list.append(resume)
        interview_ym_list = Interview.objects.filter(interview_status="YM",enterprice=request.user.enterprice_set.all()[0])
        for applier in interview_ym_list:
            resume = applier.user.resume_set.all()[0]
            resume_list.append(resume)
        return render(request, 'interviews_record.html',{"interview_jm_list":interview_jm_list,"interview_ym_list":interview_ym_list,"resume_list":resume_list})



class InterviewResultView(LoginRequiredMixin,View):
    '''面试结果'''
    def get(self,request,interview_id):
        interview_detail = Interview.objects.get(id=interview_id)
        resume_info = interview_detail.user.resume_set.all()[0]
        return render(request, 'interview_result.html',{"interview_detail":interview_detail,"resume_info":resume_info})

class InterviewDetailView(LoginRequiredMixin,View):
    '''面试详情页面'''
    def get(self,request):
        return render(request, 'interview_detail.html')

class InterviewCommentView(LoginRequiredMixin,View):
    '''面试评价'''
    def get(self,request):
        return render(request, 'interview_comment.html')