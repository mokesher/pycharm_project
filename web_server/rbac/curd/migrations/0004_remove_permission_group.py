# Generated by Django 2.2.6 on 2019-11-01 07:39

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('curd', '0003_auto_20191101_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permission',
            name='group',
        ),
    ]
