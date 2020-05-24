#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stark_demo.settings')

import django

django.setup()

from app01.models import *

# list=[]
# for i in range(1,50):
#     list.append(UserInfo(name=f"root{i}",age=20))
# UserInfo.objects.bulk_create(list)
