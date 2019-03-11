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
from django.contrib import admin
from django.urls import path,include
from applyers.views import UserView,PofileView,PositionView,LagouView,MyInterviewView,LoginView,\
    RegisterView,InterviewView,ResumView,JobCustomizeView,CollectionView,DeliveryView,CompanyListView,ResumeListView,ResumDetailView,InvitationView,JobListView,\
    CompanyView,JobView,LagouView,LoginView,RegisterView,PofileView,LogoutView
from recruiters.views import RecuiterView,InterviewRecordView,InterviewCommentView,InterviewResultView,ResumeCollectionView,\
CommentView,DeliveryRecuiterView,OfferView,OfferDetailView,InterviewDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lagou/', LagouView.as_view(), name="lagou_page"),
    path('login/', LoginView.as_view(), name="login_page"),
    path('register/', RegisterView.as_view(), name="register_page"),
    path('profile/', PofileView.as_view(), name="profile_page"),
    path('lagou/', LagouView.as_view(), name="lagou_page"),
    path('user/', UserView.as_view(), name="user_page"),
    path('login/', LoginView.as_view(), name="login_page"),
    path('register/', RegisterView.as_view(), name="register_page"),
    path('profile/', PofileView.as_view(), name="profile_page"),
    path('joblist/', JobListView.as_view(), name="job_list_page"),
    path('position/', PositionView.as_view(), name="search_page"),
    path('company/', CompanyView.as_view(), name="company_page"),
    path('myinterview/', MyInterviewView.as_view(), name="myinterview_page"),
    path('interviews/', InterviewView.as_view(), name="interview_page"),
    path('invitations/', InvitationView.as_view(), name="invitation_page"),
    path('companylist/', CompanyListView.as_view(), name="company_list_page"),
    path('job/', JobView.as_view(), name="job_page"),
    path('deliveries/', DeliveryView.as_view(), name="delivery_page"),
    path('resume/detail/', ResumDetailView.as_view(), name="resume_detail_page"),
    path('job_customize/', JobCustomizeView.as_view(), name="job_customize_page"),
    path('collections/', CollectionView.as_view(), name="collections_page"),
    path('resume/', ResumView.as_view(), name="resume_page"),
    path('resumelist/', ResumeListView.as_view(), name="resume_list_page"),
    path('interview/record', InterviewRecordView.as_view(), name="interview_record_page"),
    path('interview/detail', InterviewDetailView.as_view(), name="interview_detail_page"),
    path('interview/result', InterviewResultView.as_view(), name="interview_result_page"),
    path('interview/comment', InterviewCommentView.as_view(), name="interview_comment_page"),
    path('offer/', OfferView.as_view(), name="offer_page"),
    path('offer/detail', OfferDetailView.as_view(), name="offer_detail_page"),
    path('recruiter/deliveries', DeliveryRecuiterView.as_view(), name="delivery_recruiter_page"),
    path('recruiter/', RecuiterView.as_view(), name="recruiter_page"),
    path('comments/', CommentView.as_view(), name="comment_page"),
    path('resume/collection', ResumeCollectionView.as_view(), name="resume_collection_page"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
]