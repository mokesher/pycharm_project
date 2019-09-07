#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os,sys

for i,j,k in os.walk("1"):
	for text in k:
		path = os.path.join(i,text)
		with open(path,encoding="utf-8") as f:
			print(f.read())
