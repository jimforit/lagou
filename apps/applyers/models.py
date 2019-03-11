#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\25 17:35'

from django.db import models
from datetime import datetime
from recruiters.models import Position,EnterPrice

class Role(models.Model):
    role_choices = (
        ('user', '求职者'),
        ('recruiter', '招聘人')
    )
    id = models.AutoField('角色ID',primary_key=True)
    name = models.CharField('角色名',choices=role_choices,max_length=10)
    add_time = models.DateTimeField('注册时间', default=datetime.now)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class User(models.Model):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    id = models.AutoField('用户ID',primary_key=True)
    nick_name = models.CharField('昵称', max_length=50, default='')
    password = models.CharField('密码',max_length=20)
    gender = models.CharField('性别', max_length=10, choices=gender_choices, default='female')
    email = models.EmailField('电邮地址', max_length=64, default='')
    role = models.ForeignKey(Role, verbose_name='角色', on_delete=models.CASCADE,default=1)
    mobile = models.CharField('手机号', max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y%m', default='/static/images/CgotOVsDfHCAC9pmAAGCQkZqi4Y202.png', max_length=100)
    add_time = models.DateTimeField('注册时间', default=datetime.now)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name


class Resumer(models.Model):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )
    degree_choices = (
        ('BK','本科'),
        ('SS','硕士'),
        ('BS','博士'),
        ('DZ','大专'),
        ('GZ','高中'),
        ('MBA','MBA'),
        ('CZ', '初中'),
    )
    job_type_choice=(
        ('QZ','全职'),
        ('JZ','兼职'),
    )
    current_status_choice=(
        ('LZ','我目前已离职，可快速到岗'),
        ('ZZKL','我目前在职，考虑其他机会'),
        ('ZZBK','我目前在职，不考虑机会'),
    )
    id = models.AutoField('简历ID',primary_key=True)
    name = models.CharField('昵称', max_length=50, default='')
    creer_time = models.IntegerField('工作年限', default=0)
    gender = models.CharField('性别', max_length=10, choices=gender_choices, default='male')
    age = models.IntegerField('年龄',null=True,blank=True)
    city = models.CharField('城市', max_length=20, null=True, blank=True)
    mobile = models.CharField('手机',max_length=20)
    email = models.EmailField('邮箱地址',max_length=30)
    school = models.CharField('毕业院校',max_length=64)
    degree = models.CharField('最高学历',max_length=10,choices=degree_choices,default="BK")
    major = models.CharField('专业',max_length=64)
    self_desc = models.TextField('自我描述')
    lastest_job_desc = models.TextField('最近一份工作描述')
    lastest_job_position = models.TextField('最近一份工作职称')
    desire_position = models.CharField('期望职位',max_length=32)
    job_type = models.CharField('工作性质',choices=job_type_choice,max_length=2,default='QZ')
    desire_monthly_salary = models.CharField('期望月薪',max_length=16,null=True,blank=True)
    desire_city = models.CharField('期望城市',max_length=32,null=True,blank=True)
    current_status =models.CharField('当前状态',max_length=4,default='LZ')
    speciality = models.TextField('特长优势')
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    add_time = models.DateTimeField('创建时间',default=datetime.now)

    class Meta:
        verbose_name = '我的简历'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nick_name

class Interview(models.Model):
    interview_status_enum=(
        ('YM','已面试'),
        ('JM','将面试'),
        ('LY', '录用'),
        ('WLY', '未录用'),
    )
    id = models.AutoField('面试ID',primary_key=True)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    interview_arrangement = models.TextField('面试安排')
    interview_status = models.CharField('面试状态',choices=interview_status_enum,max_length=2,default='JM')
    add_time = models.DateTimeField('创建时间', default=datetime.now)

    class Meta:
        verbose_name = '面试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position


class Delivery(models.Model):
    delivery_enum=(
        ('YQ','邀请面试'),
        ('WJ','婉拒')
    )
    id = models.AutoField('投递ID',primary_key=True)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    add_time = models.DateTimeField('投递时间', default=datetime.now)
    delivery_status=models.CharField('投递状态',choices=delivery_enum,max_length=2)

    class Meta:
        verbose_name = '面试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position

class Collection(models.Model):
    collection_enum=(
        ('WX','无效'),
        ('YX','有效')
    )
    id = models.AutoField('收藏ID',primary_key=True)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    add_time = models.DateTimeField('创建时间', default=datetime.now)
    collection_status=models.CharField('收藏状态',choices=collection_enum,max_length=2)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position
