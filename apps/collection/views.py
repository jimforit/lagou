from django.shortcuts import render,reverse,redirect
from django.views import View
from db.login_mixin import LoginRequiredMixin

# Create your views here.
class CollectionView(LoginRequiredMixin,View):
    '''收藏列表'''
    def get(self,request):
        if request.user.role.name == "recruiter":
            return redirect(reverse("resume:resume_collection_page"))
        return render(request, 'collections.html')
