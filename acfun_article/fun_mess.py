#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,re,json,threading,time,os,random


def acfun(url, headers):
    conn_list = requests.get(url,headers=headers).text

    article_list = json.loads(conn_list)['data']['data']

    do_thread = threading.Thread(target=do, args=(article_list,))
    do_thread.start()
    do_thread.join()


def do(article_list):
    for num in article_list:
        id = num['id']
        article_title = num['title']
        open_url = "http://www.acfun.cn/v/ac" + str(id)
        print(open_url,article_title)
        url = "http://www.acfun.cn/v/ac{}".format(id)
        article_url = "http://www.acfun.cn/comment/list?isNeedAllCount=true&" \
                      "isReaderOnlyUpUser=false&isAscOrder=false&" \
                      "contentId={}&currentPage={page}".format(id,page=1)

        article_con = requests.get(article_url,headers=headers).text
        article_list = json.loads(article_con)["data"]
        total_page = article_list["totalPage"] + 1
        for page in range(1,total_page):
            article_url = "http://www.acfun.cn/comment/list?" \
                          "isNeedAllCount=true&isReaderOnlyUpUser=false&" \
                          "isAscOrder=false&contentId={}&currentPage={}".format(id, page)

            article_txt = article_list["commentContentArr"]
            for data in article_txt:
                user_name = article_txt[data]["userName"]
                if user_name == "***":
                    print("有我评论", url)
                    print(article_txt[data]["content"])

                    with open("%s.txt" % id, 'w+', encoding="utf-8") as article_write:
                        article_write.write(url + '\n')
                        article_write.write(article_txt[data]["content"] + '\n')
                        article_write.write(open_url + '\n')


for num in range(255,500):
    url = "http://www.acfun.cn/list/getlist?channelId=86&sort=1&pageSize=20&pageNo={}&startDate=1549036800000&endDate=1552060799000".format(num)

    headers = {}
    # Acfun(url,headers)
    print("第%s页"%num)

    article_thread = threading.Thread(target=acfun,args=(url,headers))
    article_thread.start()
    article_thread.join()

