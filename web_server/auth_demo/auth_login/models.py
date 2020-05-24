from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    phone = models.IntegerField()
    addr = models.CharField(max_length=16)
