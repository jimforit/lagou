# Generated by Django 2.0.2 on 2019-03-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnterPrice',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='企业ID')),
                ('name', models.CharField(max_length=50, verbose_name='企业名称')),
                ('product_desc', models.TextField(verbose_name='产品介绍')),
                ('enterprice_desc', models.TextField(verbose_name='产品介绍')),
                ('enterprice_gm', models.CharField(default='50-99人', max_length=20)),
                ('enterprice_type', models.CharField(default='移动互联网', max_length=20, verbose_name='所属行业')),
                ('finance_stage', models.CharField(default='不需要融资', max_length=10, verbose_name='融资阶段')),
                ('logo', models.ImageField(upload_to='enterprice/%Y/%m', verbose_name='logo')),
                ('address', models.CharField(max_length=150, verbose_name='企业地址')),
                ('city', models.CharField(max_length=20, verbose_name='城市')),
            ],
            options={
                'verbose_name': '企业',
                'verbose_name_plural': '企业',
            },
        ),
    ]
