#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time,requests
import json,re
from bs4 import BeautifulSoup
from pymysql_func.models import *
from threading import Thread

headers = {"Cookie": "wbilang_10000=zh_CN; mb_reg_quick=1; pgv_pvid=4271790720; ts_uid=4216851265; pgv_pvi=9810223104; ptui_loginuin=1017109861; RK=SXKFo494NT; ptcz=870fd2d6f2260c75642ff2d43748e1dd19710162eaefb2e30277c3434aeee3d3; luin=o1017109861; p_luin=o1017109861; wbilang_1017109861=zh_CN; o_cookie=1017109861; wb_regf=%3B0%3B%3Bapi.t.qq.com%3B0; pgv_info=ssid=s2393695422; mb_reg_from=8; _qpsvr_localtk=0.9513530639586689; pgv_si=s1963883520; ptisp=ctc; uin=o1017109861; skey=@LHOCT7eDA; lskey=00010000be1a7496b3288ab00f10d2882f9fdfc93bd017a31e77043323be21837888f7c34e2fe505ecba54ca; p_uin=o1017109861; pt4_token=*GF2H943v9Yqhspmjq2XWLUl-J0WYcH9Nd7X2p*L44A_; p_skey=*0Bnlmj-TW7FN8fXtwRTnzYmBbJJR4J8ENoGDm9boGk_; p_lskey=00040000045d4658ed4b6e41fd6b2c19d80f3639960b444bf92e7f55a147c044e2d716fe4c043ea7e39a405a; myhomeLowQuality=wangxin6510; ts_last=t.qq.com/w924989836",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36","Referer": "http://api.t.qq.com/proxy.html"}


def run():
    url = "http://t.qq.com/wanyingxun111?mode=0&id=383609007823221&pi=3&time=1440383216"
    res = requests.get(url, headers=headers).text
    print(res)


def con(url,page,side):
    text = json.loads(requests.get(url, headers=headers).text)
    print(page)
    html = text["info"]
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all(class_='userPic')
    for li in res:
        res = li.find_all('a', href=True)[0]
        href = res.get("href").strip("/")
        title = res.get("title").split("(")[0]
        if side == "fans":
            tosql_fans(name,href,title,page)
        else:
            tosql_follow(name,href, title, page)


name = "four4leaves"
html = requests.get(f"http://t.qq.com/{name}",headers=headers).text
soup = BeautifulSoup(html, 'html.parser')
Fans = soup.find_all(attrs={"boss": "btnApolloFollower"})[0].find('span',class_="text_count").text
Follow = soup.find_all(attrs={"boss": "btnApolloFollowing"})[0].find('span',class_="text_count").text
print("*******fans:",Fans,"***********Follow:",Follow)
fans_page = int(int(Fans)/15+2)
follow_page = int(int(Follow)/15+2)

fans_list = []
for page in range(1,fans_page):

    fans_url = f"http://api.t.qq.com/relations/follow_apollo.php?" \
          f"u={name}&t=2&st=1&p={page}&apiType=14&apiHost=" \
          f"http://api.t.qq.com&_r={100*int(time.time())}&g_tk=282436490"

    t = Thread(target=con,args=(fans_url,page,"fans"))
    t.start()



follow_list = []
for page in range(1,follow_page):

    follow_url = f"http://api.t.qq.com/relations/follow_apollo.php?" \
                 f"u={name}&t=1&st=1&p={page}&apiType=14&apiHost=" \
                 f"http://api.t.qq.com&_r={100*int(time.time())}&g_tk=353249867"
    t = Thread(target=con,args=(follow_url,page,"follow"))
    t.start()


