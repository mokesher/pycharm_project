# Generated by Django 2.2.3 on 2019-08-27 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0002_userinfo_create_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='last_mod_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间'),
        ),
    ]
