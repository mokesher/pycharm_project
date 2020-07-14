#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests,re,os
from urllib.parse import unquote
import threading
header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
head = "https://pan.rruu.net/?/%E9%9F%B3%E4%B9%90%E5%88%86%E4%BA%AB/%E5%91%A8%E6%9D%B0%E4%BC%A6%20-%20%E5%85%A8%E9%83%A8%E4%B8%93%E8%BE%91%EF%BC%88%E6%97%A0%E6%8D%9F%E6%88%96320K%EF%BC%89/"

mh = "https://pan.rruu.net"

resp = requests.get(head).text

url_list = re.findall('<i class="mdui-icon material-icons">folder_open</i>(.*?)</div>', resp, re.S)

rest = [ i.strip() for i in url_list]

def down(mp_path, url):
    try:
        if os.path.exists(mp_path):
            fsize = os.path.getsize(mp_path)
            if fsize > 1000:
                return
        with open(mp_path, "wb") as fp:
            print(f"-------down:{mp_path}")
            r = requests.get(url, headers=header)
            fp.write(r.content)
    except:
        print(f"eroor{mp_path}")

for url in rest:
    rep = requests.get(head+url).text
    mp_list = re.findall('<a href="(.*?flac|.*?mp3)" target="_blank">', rep)
    print(mp_list)
    for m in mp_list:
        name = unquote(m.rsplit("/", 1)[-1])
        print(name)
        if name.find("live") >= 0 or name.find("Live") >= 0 or name.find("mp4") >= 0 or name.find("FLV") >= 0:
            print(f"skip---{name}")
            continue
        path = os.path.join("./mp3", url)
        print(path)
        if not os.path.exists(path):
            os.mkdir(path)
        url1 = mh+m
        mp_path = os.path.join(path, name)
        down(mp_path, url1)
        # threading.Thread(target=down,args=(path, name, url1)).start()