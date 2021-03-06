# Generated by Django 2.0.2 on 2019-03-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='收藏ID')),
                ('is_valid', models.CharField(choices=[('WX', '无效'), ('YX', '有效')], max_length=2, verbose_name='收藏状态')),
            ],
            options={
                'verbose_name': '收藏',
                'verbose_name_plural': '收藏',
            },
        ),
    ]
