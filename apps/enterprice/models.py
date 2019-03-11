from django.db import models
from db.base_model import BaseModel
from user.models import User
# Create your models here.
class EnterPrice(BaseModel):
    id = models.AutoField('企业ID',primary_key=True)
    name = models.CharField('企业名称',max_length=50)
    product_desc = models.TextField('产品介绍')
    enterprice_desc = models.TextField('产品介绍')
    enterprice_gm = models.CharField(max_length=20, default="50-99人")
    enterprice_type = models.CharField(max_length=20,verbose_name="所属行业",default='移动互联网')
    finance_stage = models.CharField(max_length=10,  verbose_name="融资阶段", default="不需要融资")
    logo = models.ImageField('logo',upload_to='enterprice/%Y/%m',max_length=100)
    address = models.CharField('企业地址',max_length=150,)
    city = models.CharField('城市',max_length=20,)
    user = models.ForeignKey(User,verbose_name="用户",on_delete=models.CASCADE)

    class Meta:
        verbose_name = '企业'
        verbose_name_plural = verbose_name

    def get_position_nums(self):
        #获取发布的求职岗位数量
        return self.position_set.all().count()

    def __str__(self):
        return self.name