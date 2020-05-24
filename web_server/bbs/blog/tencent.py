#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from bs4 import BeautifulSoup
from django.http import JsonResponse
import requests, json, re

headers = {
    "Cookie": "pgv_pvi=6455973888; RK=QKgYiK89Qd; ptcz=d97378a9a74b99666b7ec9474680631cf5bdfbac77a5601c7a7a74a439edd5ed; pgv_pvid=5353233199; eas_sid=A1n5b6M2z3T9M1w8h7O5F5L0n4; ied_qq=o0168351430; tvfe_boss_uuid=df4aa1d6263c3cb5; uin_cookie=o0168351430; LW_sid=81F5O6q6L1g1f9E664R3t5S8s5; LW_uid=u1A5o6Y6R171J9M6J4h3g5z8Q6; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216cfc6bc2d5231-031f658bcf8d8d-36664c08-2073600-16cfc6bc2da925%22%2C%22%24device_id%22%3A%2216cfc6bc2d5231-031f658bcf8d8d-36664c08-2073600-16cfc6bc2da925%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; ts_uid=5120540616; Qs_lvt_323937=1568449451; Qs_pv_323937=4519110878180788700; _ga=GA1.2.1253772218.1568449452; pac_uid=1_168351430; psrf_qqrefresh_token=A9F40216D4C9AF465CE4ED03341F708B; psrf_qqunionid=A35E3CEC515D3B98B25E0438A187C533; qm_keyst=Q_H_L_2CSmQs50eSBhpV1SPgqv4O4h5lFAyzlMT3_wn8pmY5a6XDilJr5RPz2Ogi2TSqB; psrf_musickey_createtime=1570423235; psrf_qqopenid=C69A1E4FDA8980CE77C8341E92774B3E; psrf_qqaccess_token=64DEEF08825F682F49E158A7C6262938; psrf_access_token_expiresAt=1578199235; ptui_loginuin=1017109861; pgg_uid=689451929; pgg_appid=101503919; pgg_openid=5513889D7A971D103F600AB9364F9D6E; pgg_access_token=76217E51EB7AC8431C355464DB20549A; pgg_type=1; pgg_user_type=5; myhomeLowQuality=wangxin6510; ts_refer=k.t.qq.com/k/%2525E6%252584%25258F%2525E8%2525A7%252581%2525E5%25258F%25258D%2525E9%2525A6%252588; ts_uid=5120540616; ts_refer=p.t.qq.com/m/home_userinfo.php; wbilang_10000=zh_CN; pgv_info=ssid=s3444130124; mb_reg_from=8; _qpsvr_localtk=0.956457079590803; pgv_si=s7609110528; ptisp=ctc; ts_last=t.qq.com/; wbilang_1017109861=zh_CN; o_cookie=168351430; uin=o1017109861; skey=@BElUfKJje; luin=o1017109861; p_uin=o1017109861; p_luin=o1017109861; lskey=00010000dd5ce62532023f23c7b42b5c0227dfe6ea5de54ae30f1f8ba37c9d76e8f751b1365a75fbd456d373; pt4_token=dJ6o3YSaUArdmqhlcdlIEbEJKQyBqilWXzudom7mzcg_; p_skey=Ga5F84AloTjYiJ2p5Edc2IrwQJkdJNZNoFnMIoryrd8_; p_lskey=00040000cc0eb5662c25e482e142b5c06464684183dfba45639c30fb195778c1342ea6473538d0eaed732b5b; wb_regf=%3B0%3B%3Bapi1.t.qq.com%3B0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Referer": "http://api.t.qq.com/proxy.html"}


def tencent_blog(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        username = request.POST.get("username")

        url = "http://t.qq.com/" + username
        html = requests.get(url, headers=headers).text

        if "您的页面暂时无法找到" in html:
            ret["status"] = 1
            ret["msg"] = "您的页面暂时无法找到"
            print("error")
            return JsonResponse(ret)
        else:
            # blog_list = get_tencent_blog(username,html)
            blog_list = [{'href': 'qianmo2478', 'title': '浅沫'}, {'href': 'shouji136454071129', 'title': '李鑫'},
                         {'href': 'chensili8759', 'title': '陈思利'}, {'href': 'yincheng5428', 'title': '殷程'},
                         {'href': 'mayiren2712', 'title': '马伊人'}, {'href': 'tantejie6271', 'title': '忐忑姐'}]
            ret["msg"] = blog_list
            return JsonResponse(ret)

    if request.method == "GET":
        return render(request, "tencent.html")


def get_tencent_blog(username, html):
    global blog_list
    blog_list = []
    soup = BeautifulSoup(html, 'html.parser')
    Fans = soup.find_all(attrs={"boss": "btnApolloFollower"})[0].find('span', class_="text_count").text
    fans_page = int(int(Fans) / 15 + 2)
    from threading import Thread
    threading_list = []
    for page in range(1, fans_page):
        print(page)
        t = Thread(target=run, args=(username, page))
        t.start()
        threading_list.append(t)
    for i in threading_list:
        i.join()

    return blog_list


def run(username, page):
    fans_url = f"http://api.t.qq.com/relations/follow_apollo.php?" \
               f"u={username}&t=2&st=1&p={page}&apiType=14&apiHost=" \
               f"http://api.t.qq.com&_r={100 * int(time.time())}&g_tk=282436490"

    text = json.loads(requests.get(fans_url, headers=headers).text)
    html = text["info"]
    soup = BeautifulSoup(html, 'html.parser')
    res = soup.find_all(class_='userPic')
    for li in res:
        res = li.find_all('a', href=True)[0]
        href = res.get("href").strip("/")
        title = res.get("title").split("(")[0]
        blog_dict = {}
        blog_dict["href"] = href
        blog_dict["title"] = title
        blog_list.append(blog_dict)
