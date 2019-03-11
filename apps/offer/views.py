from django.shortcuts import render
from django.views import View
from db.login_mixin import LoginRequiredMixin
from interview.models import Interview

# Create your views here.

class OfferView(LoginRequiredMixin,View):
    '''Offer提交页面'''
    def get(self,request,interview_id):
        interview = Interview.objects.get(id=interview_id)
        resume = interview.user.resume_set.all()[0]
        return render(request, 'offer.html',{"interview":interview,"resume":resume})

class OfferDetailView(LoginRequiredMixin,View):
    '''招聘需求页面'''
    def get(self,request):
        return render(request, 'offer_detail.html')

