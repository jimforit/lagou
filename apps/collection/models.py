from django.db import models
from db.base_model import BaseModel
from user.models import User
from job.models import Position
from enterprice.models import EnterPrice
# Create your models here.
class Collection(BaseModel):
    collection_enum=(
        ('WX','无效'),
        ('YX','有效')
    )
    id = models.AutoField('收藏ID',primary_key=True)
    user = models.ForeignKey(User,verbose_name='用户',on_delete=models.CASCADE)
    position = models.ForeignKey(Position,verbose_name = '职位',on_delete=models.CASCADE)
    enterprice = models.ForeignKey(EnterPrice,verbose_name = '企业',on_delete=models.CASCADE)
    is_valid=models.CharField('收藏状态',choices=collection_enum,max_length=2)

    class Meta:
        verbose_name = '收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.enterprice,self.position