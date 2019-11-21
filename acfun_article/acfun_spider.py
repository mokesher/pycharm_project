#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,re,json,threading,time,random
from models import tosql

def Acfun(url,headers):
    conn_list = json.loads(requests.get(url,headers=headers).text)['data']['data']
    for conn in conn_list:
        ac_id = conn['id']
        title = conn['title']
        comment_count = conn['commentCount']
        url = "http://www.acfun.cn/v/ac" + str(ac_id)
        print(url, title)

        total_page = int(comment_count/50) + 1
        print("total_page",total_page)
        for page in range(1, total_page+1):
            if page > 80 :
                break
            print(page)
            req_url = f"https://www.acfun.cn/rest/pc-direct/comment/" \
                          f"listByFloor?sourceId={id}&sourceType=3&page={page}&" \
                          f"pivotCommentId=0&newPivotCommentId=0&_ts={int(100*time.time())}"
            down(title, req_url, url,page)


def down(article_title, req_url, url, page):
    article_con = json.loads(requests.get(req_url, headers=headers).text)

    article_txt = article_con["commentsMap"]
    for data in article_txt:
        user_name = article_txt[data]["userName"]
        content = article_txt[data]["content"]
        if user_name == "去无的止境":
            print("评论:", url)
            print("page:", page)
            print(content)

            tosql(article_title,page,content,url)




headers = {"cookie": "_did=web_4897307257E9175A; uuid=a4d9f4b1b40b825bfb5db00e71224f36; analytics=GA1.2.510850206.1569591474; analytics_gid=GA1.2.276325092.1569591474; acPasstoken=ChVpbmZyYS5hY2Z1bi5wYXNzdG9rZW4ScIlgj5-l47EyqmvuaoTLanhS8oYL1rzl5w7bibiuJ64m4LViInq6RBnXdGc8gfJUDU4Gjq8_wNo3Zf36KQOsK1R7hVdq_GdNqZF1DNrWEhXGFULgL6EbLnHF5hRsHGhGBn6sznWBlcVmZPVlG_F83GAaEv_ytBX1SUzuojzfT3qKAFJ3CCIgAItyTT_RGpx_Q6vL2ONCBa6QddRfe4agU1xxQvscEysoBTAB; auth_key=2288074; ac_username=%E5%8E%BB%E6%97%A0%E7%9A%84%E6%AD%A2%E5%A2%83; acPostHint=754d6621881f20c16146ea7c3f1f6fdfd8bd; ac_userimg=https%3A%2F%2Fimgs.aixifan.com%2Fstyle%2Fimage%2F201907%2FJxEr3ZIxcFAOe91TW3bxRTUA7h1cKstr.jpg; safety_id=AAGXiqIRrUV7IgNliiRZPBF9; session_id=182968981A25EB3A; clientlanguage=zh_CN; online_status=0; userGroupLevel=1; checkMobile=1; checkEmail=1; notice_status=1; _gat_UA-68793632-3=1; Hm_lvt_2af69bc2b378fb58ae04ed2a04257ed1=1569593030; cur_req_id=59970295AC67271_self_b4b3b5fe312ca69b9a29fe80575a8374; cur_group_id=59970295AC67271_self_b4b3b5fe312ca69b9a29fe80575a8374_0; Hm_lpvt_2af69bc2b378fb58ae04ed2a04257ed1=1569593044",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

for page in range(1, 500):
    print("第%s页：" %page)
    url = f"https://www.acfun.cn/list/getlist?channelId=86&" \
          f"sort=1&pageSize=20&pageNo={page}"
    Acfun(url, headers)

