#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import time,requests
import json,re
from bs4 import BeautifulSoup
from pymysql_func.models import *
from threading import Thread

headers = {"Cookie": "pgv_pvi=5701005312; pgv_pvid=864805164; ptui_loginuin=1017109861; RK=gfKN9Y9YOz; ptcz=52b3b747eed0e8067b897cdbf5d6a23e8e1cee850fea59c0b480cc2a8d66c36c; wbilang_10000=zh_CN; o_cookie=1017109861; ts_uid=4463014641; wbilang_1017109861=zh_CN; myhomeLowQuality=wangxin6510; ts_refer=search.t.qq.com/user.php; mb_reg_quick=1; pgv_info=ssid=s6347911065; mb_reg_from=8; _qpsvr_localtk=0.6715166861908659; pgv_si=s8607945728; ptisp=ctc; uin=o1017109861; skey=@17yE1qSFA; luin=o1017109861; lskey=00010000835842874f4545933e1aaa88f74ec0897ef69ff28398a1feb14059a882140d98ec8658e17a46cb11; p_uin=o1017109861; pt4_token=EsJ-eawlLvXGMwAvDRrcbJwPI6X6FNO1WHvdtMO0l38_; p_skey=aBGoPOcXBkJKvWMvoU2MofeWQE4hEuUsRZFgWkL4oeI_; p_luin=o1017109861; p_lskey=0004000098ff213510b15cf9c064eaeacad709a929df226f61f422765556b8590e58279d9ab6d96bca223a52; wb_regf=%3B0%3B%3Bapi.t.qq.com%3B0; ts_last=t.qq.com/ywjh1172862577",
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


name = "LDY569616474"
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


