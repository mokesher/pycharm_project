#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests,re,time

headers = {}

url = "http://t.qq.com/user/mine"
page = range(50)
for pa in page:
	con = requests.get(url, headers=headers).text
	file_text = re.findall(r'<div class="msgCnt">(.*?)</div><div class="pubInfo', con)
	print(file_text)

	con = requests.get(url, headers=headers).text
	id = re.findall(r'</span><a href="(.*?)" class="pageBtn">',con)[0]
	url = "http://t.qq.com/user/mine{}".format(id)
	print(url)

