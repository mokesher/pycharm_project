#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests,re,json,threading,time,random

headers = {"*******"}

def Acfun(url,headers):
    conn_list = requests.get(url,headers=headers).text
    print(conn_list)
    article_list = json.loads(conn_list)['data']['articleList']
    for num in article_list:
        # print(num)
        id = num['id']
        article_title = num['title']
        open_url = "http://www.acfun.cn/v/ac" + str(id)
        print(open_url, article_title)
        url = "http://www.acfun.cn/v/ac{}".format(id)

        article_url = "http://www.acfun.cn/comment/list?isNeedAllCount=true&" \
                      "isReaderOnlyUpUser=false&isAscOrder=false&contentId={}&" \
                      "currentPage={page}".format(id,page=1)
        article_con = requests.get(article_url,headers=headers).text
        article_list = json.loads(article_con)["data"]
        total_page = article_list["totalPage"] + 1

        for num in range(1,total_page):
            article_url = "http://www.acfun.cn/comment/list?isNeedAllCount=true&" \
                          "isReaderOnlyUpUser=false&isAscOrder=false&" \
                          "contentId={}&currentPage={}".format(id,num)
            article_txt = article_list["commentContentArr"]
            for data in article_txt:
                user_name = article_txt[data]["userName"]
                if user_name == "***":
                    print(url)
                    print(article_txt[data]["content"])

                    with open("1/%s.txt" % id, 'w+', encoding="utf-8") as article_write:
                        article_write.write(url + '\n')
                        article_write.write(article_txt[data]["content"] + '\n')
                        article_write.write(open_url + '\n')


for num in range(400,500):
    url = "http://webapi.aixifan.com/query/article/list?" \
          "pageNo={}&size=10&realmIds=25%2C34%2C7%2C6%2C17%2C1%2C2&" \
          "originalOnly=false&orderType=1&periodType=-1&filterTitleImage=true".format(num)

    Acfun(url, headers)
    print("第%s页："%num)
