from django.db import models
from db.base_model import BaseModel
from job.models import Position
from enterprice.models import EnterPrice
# Create your models here.
class Offer(BaseModel):
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
    offer_status=models.CharField('offer状态',choices=offer_enum,max_length=2,default='WX')

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position,self.salary,self.offer_status
