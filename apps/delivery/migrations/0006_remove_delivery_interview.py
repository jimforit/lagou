# Generated by Django 2.0.2 on 2019-03-10 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_delivery_enterprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='interview',
        ),
    ]