from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(BaseModel):
    role_choices = (
        ('user', '求职者'),
        ('recruiter', '招聘人')
    )
    id = models.AutoField('角色ID',primary_key=True)
    name = models.CharField('角色名',choices=role_choices,max_length=10)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class User(AbstractUser,BaseModel):
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

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
