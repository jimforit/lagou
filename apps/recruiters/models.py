#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = 'jimit'
__CreateAt__ = '2019\2\23 21:09'

from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class EnterPrice(models.Model):
    EP_CHOICES = (
        ("JXQY", "10-49人"),
        ("XQY", "50-99人"),
        ("ZXQY", "100-499人"),
        ("ZQY", "500-1000人"),
        ("DQY", "1000-5000人"),
        ("JT", "5000人以上"),
    )
    FINANCE_SG=(
        ("WRZ","未融资"),
        ("TSL", "天使轮"),
        ("AL","A轮"),
        ("BL","B轮"),
        ("CL","C轮"),
        ("BXY","不需要融资")
    )
    EP_TYPE = (
        ("MI", "移动互联网"),
        ("ET", "电信"),
        ("FT", "金融"),
        ("DS", "电商"),
        ("ZQ", "证券"),
        ("WLW", "物联网")
    )
    id = models.AutoField('企业ID',primary_key=True)
    name = models.CharField('企业名称',max_length=50)
    product_desc = models.TextField('产品介绍')
    enterprice_desc = models.TextField('产品介绍')
    enterprice_gm = models.CharField(max_length=20, choices=EP_CHOICES, default="XQY")
    enterprice_type = models.CharField(max_length=20,choices=EP_TYPE, verbose_name="所属行业",default='MI')
    finance_stage = models.CharField(max_length=10, choices=FINANCE_SG, verbose_name="融资阶段", default="BXY")
    logo = models.ImageField('logo',upload_to='enterprice/%Y/%m',max_length=100)
    address = models.CharField('企业地址',max_length=150,)
    city = models.CharField('城市',max_length=20,)
    add_time = models.DateTimeField('创建时间',default=datetime.now)

    class Meta:
        verbose_name = '企业'
        verbose_name_plural = verbose_name

    def get_position_nums(self):
        #获取发布的求职岗位数量
        return self.position_set.all().count()

    def __str__(self):
        return self.name

class Position(models.Model):
    position_type_choice = (
        ('QZ', '全职'),
        ('JZ', '兼职'),
    )
    experience_range=(
        ('YJ','应届生'),
        ('XS','1-3年'),
        ('ZJ','3-5年'),
        ('GJ','5-7年'),
        ('ZJ','7年以上'),
        ('DK','10年以上'),
    )
    degree_choices = (
        ('BK', '本科'),
        ('SS', '硕士'),
        ('BS', '博士'),
        ('DZ', '大专'),
        ('GZ', '高中'),
        ('MBA', 'MBA'),
        ('CZ', '初中'),
    )
    position_status_enum = (
        ('YX', '有效'),
        ('WX', '无效'),
    )
    id = models.AutoField('职位ID',primary_key=True)
    name = models.CharField('职称',max_length=64)
    city = models.CharField('工作城市',max_length=64)
    position_type = models.CharField('职位类型',choices=position_type_choice,max_length=2)
    experience_required = models.CharField('工作经验要求',choices=experience_range,max_length=2)
    degree_required = models.CharField('最低学历要求',choices=degree_choices,max_length=3)
    attractive_desc=models.TextField('职位诱惑',null=True,blank=True)
    position_desc = models.TextField('职位描述',null=True,blank=True)
    position_status=models.CharField('职位状态',choices=position_status_enum,max_length=2,default='YX')
    enterprice = models.ForeignKey(EnterPrice,verbose_name="企业",on_delete=models.CASCADE)
    add_time = models.DateTimeField('创建时间', default=datetime.now)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Offer(models.Model):
    offer_enum=(
        ('WX','无效'),
        ('YX','有效'),
        ('WJ', '婉拒'),
        ('AC', '接受')
    )
    id = models.AutoField('OfferID',primary_key=True)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    salary = models.CharField('薪资待遇',max_length=32)
    offer_desc = models.TextField('offer描述')
    add_time = models.DateTimeField('创建时间', default=datetime.now)
    offer_status=models.CharField('offer状态',choices=offer_enum,max_length=2,default='WX')

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position,self.salary,self.offer_status


