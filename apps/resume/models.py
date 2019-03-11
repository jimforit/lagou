from django.db import models
from db.base_model import BaseModel
from user.models import User

# Create your models here.
class Resume(BaseModel):
    id = models.AutoField('简历ID',primary_key=True)
    name = models.CharField('昵称', max_length=50, default='')
    creer_time = models.IntegerField('工作年限', default=0)
    gender = models.CharField('性别', max_length=10,default='male')
    age = models.IntegerField('年龄',null=True,blank=True)
    city = models.CharField('城市', max_length=20, null=True, blank=True)
    mobile = models.CharField('手机',max_length=20)
    email = models.EmailField('邮箱地址',max_length=30)
    school = models.CharField('毕业院校',max_length=64)
    degree = models.CharField('最高学历',max_length=10,default="本科")
    major = models.CharField('专业',max_length=64)
    self_desc = models.TextField('自我描述')
    lastest_job_desc = models.TextField('最近一份工作描述')
    lastest_job_position = models.TextField('最近一份工作职称')
    desire_position = models.CharField('期望职位',max_length=32)
    job_type = models.CharField('工作性质',max_length=2,default='全职')
    desire_monthly_salary = models.CharField('期望月薪',max_length=16,null=True,blank=True)
    desire_city = models.CharField('期望城市',max_length=32,null=True,blank=True)
    current_status =models.CharField('当前状态',max_length=4,default='已离职')
    is_public = models.IntegerField('是否开启邀约',default=0)
    speciality = models.TextField('特长优势')
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '我的简历'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name