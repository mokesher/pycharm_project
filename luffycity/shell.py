#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'luffycity.settings')

import django
django.setup()

from django.contrib.contenttypes.models import ContentType

obj = ContentType.objects.get(model="course")
print(type(obj))