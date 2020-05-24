#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CRM_SYSTEM.settings')
import django

django.setup()

from crm import models

print(dir(models))
for i in dir(models):
    if "__" not in i and i != "models":
        print(f'<a href="/stark/crm/{i.lower()}/">{i}</a>')
