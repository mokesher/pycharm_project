#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
import re
import csv


def getMovieList(urls):
    res = requests.get(urls)
    res.encoding = "GBK"
    html = res.text
    items = re.findall(r'<a href="(.*?\.html)" class="ulink">(.*?)</a>', html)
    return items


def getMovieContent(url):
    down_urls = 'http://www.ygdy8.com/{}'.format(url)
    res = requests.get(down_urls)
    res.encoding = "GBK"
    html = res.text
    down_url = re.findall(r'bgcolor="#fdfddf"><a href="(.*?)">', html)[0]
    return down_url


def excel_save(title, down_url):
    print(title, down_url)
    with open('some.csv', 'a+', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow([title, down_url])
        csvfile.close()


for page in range(1, 177):
    print("正在爬取第{}页".format(page))
    urls = "http://www.ygdy8.com/html/gndy/oumei/list_7_{}.html".format(page)
    getMovieList(urls)

    for url, title in getMovieList(urls):
        # print(url,title)
        down_url = getMovieContent(url)
        excel_save(title, down_url)
