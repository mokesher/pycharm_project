# Generated by Django 2.2.6 on 2019-10-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='library.Book')),
            ],
        ),
    ]