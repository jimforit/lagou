# Generated by Django 2.0.2 on 2019-03-08 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterprice', '0002_enterprice_user'),
        ('delivery', '0004_delivery_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='enterprice',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='enterprice.EnterPrice', verbose_name='企业'),
            preserve_default=False,
        ),
    ]
