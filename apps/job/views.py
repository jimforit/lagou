from django.shortcuts import render
from django.views import View
from db.login_mixin import LoginRequiredMixin
from .models import Position
from enterprice.models import EnterPrice
# Create your views here.
class JobCustomizeView(LoginRequiredMixin,View):
    '''岗位订阅'''
    def get(self,request):
        return render(request, 'job_customize.html')

class JobListView(View):
    '''岗位列表'''
    def get(self,request):
        position_list = Position.objects.all()
        return render(request, 'index.html',{"position_list":position_list})

class JobView(View):
    '''工作详情页'''
    def get(self,request,job_id):
        job = Position.objects.get(id=job_id)
        return render(request, 'job.html',{"job":job})

class PositionView(View):
    '''岗位信息'''
    def get(self,request):
        return render(request, 'search.html')

class RecuiterView(LoginRequiredMixin,View):
    '''招聘需求页面'''
    def get(self,request):
        return render(request, 'recruiter.html')

    def post(self,request):
        name = request.POST.get("position","")
        city = request.POST.get("city", "")
        degree_required = request.POST.get("degree_required","")
        attractive_desc = request.POST.get("attractive_desc","")
        salary = request.POST.get("salary","")
        experience_required = request.POST.get("experience_required", "")
        position_type = request.POST.get("position_type", "")
        effect_days = request.POST.get("effect_days", "")
        position_desc = request.POST.get("position_desc","")
        if not all([name,city,degree_required,attractive_desc,salary,experience_required,position_type,effect_days,position_desc]):
            message="信息输入不完整"
            return render(request, "enterpriceinfo.html", {"message": message})
        else:
            print([name,city,degree_required,attractive_desc,salary,experience_required,position_type,effect_days,position_desc])
            position = Position()
            position.name = name
            position.city = city
            position.degree_required = degree_required
            position.attractive_desc = attractive_desc
            position.salary = salary
            position.experience_required = experience_required
            position.position_type = position_type
            position.effect_days = effect_days
            position.position_desc = position_desc
            position.enterprice_id = EnterPrice.objects.get(user_id=request.user.id,is_delete=0).id
            position.save()
            message = "招聘信息发布完成"
            return  render(request,"successful.html",{"message":message})
