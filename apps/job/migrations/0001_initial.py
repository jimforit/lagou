# Generated by Django 2.0.2 on 2019-03-08 13:03

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='职位ID')),
                ('name', models.CharField(max_length=64, verbose_name='职称')),
                ('city', models.CharField(max_length=64, verbose_name='工作城市')),
                ('position_type', models.CharField(max_length=5, verbose_name='职位类型')),
                ('experience_required', models.CharField(max_length=10, verbose_name='工作经验要求')),
                ('degree_required', models.CharField(max_length=5, verbose_name='最低学历要求')),
                ('salary', models.CharField(max_length=10, verbose_name='工资范围')),
                ('attractive_desc', models.TextField(blank=True, null=True, verbose_name='职位诱惑')),
                ('position_desc', tinymce.models.HTMLField(blank=True, null=True, verbose_name='职位描述')),
                ('effect_days', models.CharField(default='一周', max_length=6, verbose_name='岗位有效期')),
                ('position_status', models.CharField(default='有效', max_length=2, verbose_name='职位状态')),
                ('enterprice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enterprice.EnterPrice', verbose_name='企业')),
            ],
            options={
                'verbose_name': '职位',
                'verbose_name_plural': '职位',
            },
        ),
    ]