from django.db import models


class Man(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=16, null=False)


class Woman(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16, null=False)
    password = models.CharField(max_length=16, null=False)


class Relation(models.Model):
    man = models.ForeignKey("Man", on_delete=models.DO_NOTHING)
    woman = models.ForeignKey("Woman", on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = [
            ("man", "woman")
        ]
