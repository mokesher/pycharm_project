#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import re

ip_list = []

with open("log.txt","r") as f:
    res = re.findall("(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)",f.read())
    for i in res:
        ip = ".".join(i)
        ip_list.append(ip)

ip = set(ip_list)
print(ip)
