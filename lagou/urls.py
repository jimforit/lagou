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
from user.views import LagouView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lagou/', LagouView.as_view(), name="lagou_page"),
    path('', LagouView.as_view(), name="lagou_page"),
    path("users/", include('user.urls', namespace="user")),
    path("offers/", include('offer.urls', namespace="offer")),
    path("resumes/", include('resume.urls', namespace="resume")),
    path("deliveries/", include('delivery.urls', namespace="delivery")),
    path("collections/", include('collection.urls', namespace="collection")),
    path("interviews/", include('interview.urls', namespace="interview")),
    path("jobs/", include('job.urls', namespace="job")),
    path("enterprices/", include('enterprice.urls', namespace="enterprice")),
]