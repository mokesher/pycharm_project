#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests, json, re
import time


def run(url):
    res = requests.get(url,headers=headers).text.split("(",1)[1].rsplit(")",1)[0]
    res = json.loads(res)["data"]["replies"]
    for i in res:
        content = i["content"]["message"]
        if "bgm" in content:
            print(content)
        elif "音乐" in content:
            print(content)
        elif "开头" in content:
            print(content)



headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
           "Cookie": "buvid3=4CBC00B3-8481-42B3-9F28-65CA304035F640758infoc; LIVE_BUVID=AUTO1815609460132182; sid=iq33m5ck; CURRENT_FNVAL=16; stardustvideo=1; rpdid=|(kmR)l)kkJu0J'ulY|mR~u|l; im_notify_type_13711265=0; UM_distinctid=16b84fc79ccb40-04b63241d1312f-36664c08-1fa400-16b84fc79cd393; im_local_unread_13711265=0; im_seqno_13711265=759; _uuid=E37A54A4-E542-301E-FBBD-CB143E4B7AA689464infoc; DedeUserID=13711265; DedeUserID__ckMd5=23b07ffc7d1107dd; SESSDATA=5b263e23%2C1571360134%2C4711c591; bili_jct=d5ce1fb269acf434fafc30957206a868; CURRENT_QUALITY=16; bp_t_offset_13711265=310545845109966839","Referer": "https://www.bilibili.com/video/av71327501"
           }

for page in range(0,100):
    print(page)
    url = f"https://api.bilibili.com/x/v2/reply?callback=jQuery17208677126098755512_1571146595675&jsonp=jsonp&pn={page}&type=1&oid=71327501&sort=2&={100*int(time.time())}"
    run(url)
