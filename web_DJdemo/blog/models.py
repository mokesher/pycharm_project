from django.db import models
from django.utils.timezone import now


class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.CharField(max_length=16)


class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.CharField(max_length=16)
    theclass = models.ForeignKey(to="Classes", on_delete=models.CASCADE())

    def __str__(self):
        return f"id:{self.id}-{self.teacher}"


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.CharField(null=False, max_length=20)
    age = models.IntegerField()
    gender_choices = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(choices=gender_choices)

    def __str__(self):
        return f"id:{self.id}-{self.student}"


class U2U(models.Model):
    b = models.ForeignKey(to="UserInfo", related_name="girls", on_delete=models.DO_NOTHING)
    g = models.ForeignKey(to="UserInfo", related_name="boys", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [
            ('b', 'g'),
        ]

