#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import urllib
import re


class QSBK:
    def __init__(self):
        self.pageindex = 1
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
        self.stories = []
        self.enable = False

    def getpage(self, pageindex):
        try:
            url = 'https://www.qiushibaike.com/hot/%s/%s' % ('page', pageindex)
            # print url
            request = urllib.Request(url, headers=self.headers)
            res = urllib.urlopen(request)
            res = res.read().decode('utf-8')
            return res
        except:
            print('链接失败错误')

    def getpageitems(self, pageindex):
        res = self.getpage(pageindex)
        if not res:
            print('页面加载失败')
            return
        pattern = re.compile(r'<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?class="number">(.*?)</i>.*?class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, res)
        # print items
        pagestories = []
        for item in items:
            pagestories.append([item[0], item[1], item[2], item[3]])
        return pagestories

    def loadpage(self):
        if self.enable == True:
            if len(self.stories) < 2:
                pagestories = self.getpageitems(self.pageindex)
                if pagestories:
                    self.stories.append(pagestories)
                    self.pageindex += 1

    def getonestory(self, pagestories, page):
        n = 0
        for story in pagestories:
            input = input('')
            n += 1
            self.loadpage()
            if input == 'q':
                self.enable = False
                return
            print('第%d页\t第%d条发布：%s\t%s' % (page, n, story[0], story[1]))
            print('这条阅读量是%s,评论是%s条' % (story[2], story[3]))

    def start(self):
        print('正在读取糗事百科，按回车查看新段子，q退出')
        self.enable = True
        self.loadpage()
        nowpage = 0
        while self.enable:
            if len(self.stories) > 0:
                pagestories = self.stories[0]
                nowpage += 1
                del self.stories[0]
                self.getonestory(pagestories, nowpage)


spider = QSBK()
spider.start()
