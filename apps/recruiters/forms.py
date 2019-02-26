#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\25 14:48'

from django import forms
from captcha.fields import CaptchaField
import re

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid': '请输入有效电子邮箱地址'})
    password = forms.CharField(required=True, min_length=8)
