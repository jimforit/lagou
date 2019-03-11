from django.shortcuts import render
from django.views import View
from db.login_mixin import LoginRequiredMixin
from enterprice.models import EnterPrice
from job.models import Position
from user.models import Role

# Create your views here.
class CompanyDetailView(View):
    '''公司详情介绍页'''
    def get(self,request,enterprice_id):
        company = EnterPrice.objects.get(id=enterprice_id)
        position_list = Position.objects.filter(enterprice_id=enterprice_id)
        return render(request, 'company.html',{"company":company,"position_list":position_list})

class CompanyView(View):
    '''公司信息填写页'''
    def get(self,request):
        return render(request, 'enterpriceinfo.html')

    def post(self,request):
        name = request.POST.get("name","")
        product_desc = request.POST.get("product_desc","")
        enterprice_desc = request.POST.get("enterprice_desc","")
        address = request.POST.get("address","")
        city = request.POST.get("city","")
        enterprice_gm = request.POST.get("enterprice_gm", "")
        finance_sg = request.POST.get("finance_sg", "")
        enterprice_ty = request.POST.get("enterprice_ty", "")
        self_image = request.POST.get("self_image", "")
        if not all([name,product_desc,enterprice_desc,address,city,enterprice_gm,finance_sg,enterprice_ty,self_image]):
            message="信息填写不完全"
            return render(request, "enterpriceinfo.html",{"message":message})
        else:
            print([name,product_desc,enterprice_desc,address,city,enterprice_gm,finance_sg,enterprice_ty,self_image])
            company_info=EnterPrice()
            company_info.name = name
            company_info.product_desc = product_desc
            company_info.enterprice_desc = enterprice_desc
            company_info.address = address
            company_info.city = city
            company_info.enterprice_gm = enterprice_gm
            company_info.finance_stage = finance_sg
            company_info.enterprice_type = enterprice_ty
            company_info.logo = '/static/images/'+self_image
            company_info.user_id=request.user.id
            company_info.save()
            user = request.user
            user.nick_name=company_info.name+"HR"
            role = Role.objects.get(id=user.role_id)
            role_recruiter = Role.objects.filter(name="recruiter").first()
            if role_recruiter is not None:
                user.role = role_recruiter
            else:
                role.name = "recruiter"
                role.save()
            user.save()
            message = "基本信息填写完成"
            return render(request,"successful.html",{"message":message})

class CompanyListView(View):
    '''公司列表页'''
    def get(self,request):
        company_list = EnterPrice.objects.filter(is_delete=0)
        return render(request, 'companylist.html',{"company_list":company_list})

class CommentView(LoginRequiredMixin,View):
    '''公司评价页'''
    def get(self,request):

        return render(request, 'comment.html')
