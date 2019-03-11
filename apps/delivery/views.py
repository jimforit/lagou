from django.shortcuts import render,reverse,redirect
from django.views import View
from db.login_mixin import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponse,JsonResponse
from .models import Delivery
from user.models import User
from job.models import Position
from interview.models import Interview
from resume.models import Resume
# Create your views here.
class DeliveryApplierView(LoginRequiredMixin,View):
    '''投递列表'''
    def get(self,request):
        if request.user.role.name == "recruiter":
            return redirect(reverse("delivery:delivery_recruiter_page"))
        #待定列表
        delivery_all_list = Delivery.objects.filter(delivery_status="DD",user_id = request.user.id)
        # 邀请列表
        delivery_yq_list = Delivery.objects.filter(delivery_status="YQ",user_id = request.user.id)
        #婉拒列表
        delivery_wj_list = Delivery.objects.filter(delivery_status="WJ",user_id = request.user.id)
        return render(request, 'deliveries.html',{"delivery_dd_list":delivery_all_list,"delivery_yq_list":delivery_yq_list,"delivery_wj_list":delivery_wj_list})

    def post(self,request):
        job_id=request.POST.get('job_id')
        delivery = Delivery.objects.filter(user_id = request.user.id,position_id=job_id).first()
        if delivery:
            return JsonResponse({'res': 0, 'errmsg': '请勿重复提交'})
        else:
            delivery = Delivery()
            delivery.user = User.objects.get(id=request.user.id)
            delivery.delivery_status = 'DD'
            delivery.position = Position.objects.get(id=job_id)
            delivery.enterprice =delivery.position.enterprice
            delivery.resume = Resume.objects.get(user_id=request.user.id)
            delivery.save()
            return JsonResponse({'res': 1, 'success': '申请发送成功'})



class DeliveryRecuiterView(LoginRequiredMixin,View):
    '''招聘者页面'''
    def get(self, request):
        # 待定列表
        delivery_dd_list = Delivery.objects.filter(delivery_status="DD",enterprice_id=request.user.enterprice_set.all()[0].id)
        # 邀请列表
        delivery_yq_list = Delivery.objects.filter(delivery_status="YQ", enterprice_id=request.user.enterprice_set.all()[0].id)
        # 婉拒列表
        delivery_wj_list = Delivery.objects.filter(delivery_status="WJ", enterprice_id=request.user.enterprice_set.all()[0].id)
        return render(request, 'deliveries_recruiter.html',{"delivery_dd_list":delivery_dd_list,"delivery_yq_list":delivery_yq_list,"delivery_wj_list":delivery_wj_list})

    def post(self,request,user_id):
        delivery = Delivery()
        delivery.user_id=user_id
        print(request.POST)
        message = "面邀已发送！"
        return render(request,"successful.html",{"message":message})

class DeliveryView(LoginRequiredMixin,View):
    '''招聘者页面'''
    def get(self,request,page=None):
        delivery_list = Delivery.objects.all()
        return render(request, 'deliveries_recruiter.html',{"delivery_list":delivery_list})

    def post(self,request,user_id):
        delivery = Delivery()
        delivery.user = User.objects.get(id=user_id)
        delivery.delivery_status = 'YQ'
        delivery.enterprice = request.user.enterprice_set.all()[0]
        delivery.position = Position.objects.get(id=int(request.POST.get("position")))
        delivery.resume = Resume.objects.get(user_id=user_id)
        delivery.save()
        new_interview = Interview()
        new_interview.position = delivery.position
        new_interview.enterprice = delivery.enterprice
        new_interview.user = delivery.user
        new_interview.delivery = delivery
        new_interview.interview_arrangement = request.POST.get("invitation")
        new_interview.save()
        message = "面邀已发送！"
        return render(request,"successful.html",{"message":message})
