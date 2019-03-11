#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\25 14:48'

from django import forms
from captcha.fields import CaptchaField
import re

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,label='密码',widget=forms.PasswordInput())

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,label='密码',widget=forms.PasswordInput())