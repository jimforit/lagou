from django.db import models
from db.base_model import BaseModel
from job.models import Position
from enterprice.models import EnterPrice
from delivery.models import Delivery
from user.models import User
# Create your models here.

class Interview(BaseModel):
    interview_status_enum=(
        ('YM','已面试'),
        ('JM','将面试'),
        ('LY', '录用'),
        ('WLY', '未录用'),
    )
    id = models.AutoField('面试ID',primary_key=True)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name = '候选人',on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery,verbose_name = '投递',on_delete=models.CASCADE)
    interview_arrangement = models.TextField('面试安排')
    interview_status = models.CharField('面试状态',choices=interview_status_enum,max_length=2,default='JM')

    class Meta:
        verbose_name = '面试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position