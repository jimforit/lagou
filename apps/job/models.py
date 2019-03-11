from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
from enterprice.models import EnterPrice
# Create your models here.
class Position(BaseModel):
    id = models.AutoField('职位ID',primary_key=True)
    name = models.CharField('职称',max_length=64)
    city = models.CharField('工作城市',max_length=64)
    position_type = models.CharField('职位类型',max_length=5)
    experience_required = models.CharField('工作经验要求',max_length=10)
    degree_required = models.CharField('最低学历要求',max_length=5)
    salary = models.CharField('工资范围',max_length=10)
    attractive_desc=models.TextField('职位诱惑',null=True,blank=True)
    position_desc = HTMLField('职位描述',null=True,blank=True)
    effect_days = models.CharField('岗位有效期',default="一周",max_length=6)
    position_status=models.CharField('职位状态',max_length=2,default='有效')
    enterprice = models.ForeignKey(EnterPrice,verbose_name="企业",on_delete=models.CASCADE)

    class Meta:
        verbose_name = '职位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name