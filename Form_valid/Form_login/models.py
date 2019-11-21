from django.db import models


class Classes(models.Model):
    title = models.CharField(max_length=16, unique=True)


class Student(models.Model):
    name = models.CharField(max_length=16)
    age = models.IntegerField()
    cls = models.ForeignKey("Classes", on_delete=models.DO_NOTHING)


class Teacher(models.Model):
    name = models.CharField(max_length=16)
    c2t = models.ManyToManyField("Classes")
