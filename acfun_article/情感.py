# -*- coding:utf-8 -*-
import requests,re,json,threading,time,os,random
from models import tosql
from login import Login


def acfun(url):
    conn_list = login_session.get(url, headers=headers).text
    article_list = json.loads(conn_list)['data']['articleList']
    # article(article_list)
    t_list = []
    for data in article_list:
        conn_thread = threading.Thread(target=article, args=(data,))
        conn_thread.start()
        t_list.append(conn_thread)
    for j in t_list:
        j.join()


def article(data):
    id = data['id']
    comment_count = data["comment_count"]
    article_title = data['title']
    url = "http://www.acfun.cn/v/ac" + str(id)
    total_page = int(comment_count/50) + 1

    for page in range(1, total_page+1):
        print(page)
        req_url = f"https://www.acfun.cn/rest/pc-direct/comment/listByFloor?sourceId={id}&sourceType=3&page={page}&pivotCommentId=0&newPivotCommentId=0&_ts={int(100*time.time())}"
        down(article_title, req_url, url,page)


def down(article_title, req_url, url, page):
    article_con = json.loads(login_session.get(req_url,headers=headers).text)
    article_txt = article_con["commentsMap"]
    for data in article_txt:
        user_name = article_txt[data]["userName"]
        content = article_txt[data]["content"]
        if user_name == "不知有汉":
            print("评论:", url)
            print("page:", page)
            print(content)

            # tosql(article_title,page,content,url)

            with open("comment/%s.txt" % article_title, 'a+', encoding="utf-8") as article_write:
                article_write.write(article_title + '\n')
                article_write.write("page:" + str(page) + '\n')
                article_write.write(content + '\n')
                article_write.write(url + '\n')


login_session = Login()
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

article_threading_list = []
for page in range(1, 1000):
    print("第%s页" % page)

    url = f"https://webapi.acfun.cn/query/article/list?pageNo={page}&size=10&realmIds=25%2C34%2C7%2C6%2C17%2C1%2C2&originalOnly=true&orderType=1&periodType=-1&filterTitleImage=true"

    acfun(url)
    t = threading.Thread(target=acfun, args=(url,))
    t.start()
    article_threading_list.append(t)

    for t in article_threading_list:
        t.join()

