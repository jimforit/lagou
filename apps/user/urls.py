#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\3\7 9:24'

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
from django.urls import path,include
from .views import UserView,PofileView,LagouView,LoginView,RegisterView,LogoutView,RoleView

app_name = 'user'

urlpatterns = [
    path('login/', LoginView.as_view(), name="login_page"),
    path('register/', RegisterView.as_view(), name="register_page"),
    path('profile/', PofileView.as_view(), name="profile_page"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
    path('logout/', LogoutView.as_view(), name="logout_page"),
    path('role/', RoleView.as_view(), name="role_page"),
]