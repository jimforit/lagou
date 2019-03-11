from django.db import models
from db.base_model import BaseModel
from enterprice.models import EnterPrice
from job.models import Position
from user.models import User
from resume.models import Resume
# Create your models here.
class Delivery(BaseModel):
    delivery_enum=(
        ('DD','待定'),
        ('YQ','邀请面试'),
        ('WJ','婉拒')
    )
    id = models.AutoField('投递ID',primary_key=True)
    resume = models.ForeignKey(Resume,verbose_name = '简历',on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name = '求职者',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice, verbose_name='企业', on_delete=models.CASCADE)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    #interview = models.ForeignKey(Interview,verbose_name = '面试',on_delete=models.CASCADE)
    delivery_status=models.CharField('投递状态',choices=delivery_enum,default="DD", max_length=2)

    class Meta:
        verbose_name = '面试'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice.name,self.user.nick_name