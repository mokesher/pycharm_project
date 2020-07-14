# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy_demo.items import Acfun_Item
import json, time, re


class AcfunSpider(scrapy.Spider):
    name = 'acfun'
    allowed_domains = ['acfun.cn']

    def start_requests(self):
        loginUrl = "https://id.app.acfun.cn/rest/web/login/signin"
        yield scrapy.FormRequest(url=loginUrl, formdata={"username": "13321270519",
                                                         "password": "hxmh23wei"},
                                                          callback = self.after_login)

    def after_login(self, response):
        print("after_login")
        # for ac in range(15925495, 2071656, -1): 14100000
        # for ac in range(15925495, 2071656, -1): 2600000 - 2700000
        # for ac in range(15925495, 2071656, -1): 3300000
        for ac in range(3400000, 3500000, 1):
            print(f"------------第ac{ac}------------")
            url = f"https://www.acfun.cn/a/ac{ac}"
            yield scrapy.Request(url=url, callback=self.acfun, meta={'ac': ac})

    def acfun(self, response):
        ac = response.meta['ac']
        res = re.findall(r"<title >(.*?) - AcFun", response.text)
        if res:
            title = res[0].strip()
            print(title)
            page_url = f"https://www.acfun.cn/rest/pc-direct/comment/listByFloor?" \
                   f"sourceId={ac}&sourceType=3&page=1&pivotCommentId=0&newPi" \
                   f"votCommentId=0&_ts={int(100 * time.time())}"
            yield scrapy.Request(url=page_url, callback=self.article,
                                meta={'title': title, "url": response.url})

    def article(self, response):
        title = response.meta['title']
        comment_req = json.loads(response.text)
        total_page = comment_req["totalPage"]
        for page in range(1, total_page+1):
            comment_url = re.sub("page=1", f"page={page}", response.url)
            yield scrapy.Request(url=comment_url, callback=self.down, dont_filter=True,
                         meta={'title': title, 'page': page, "url": response.meta['url']})

    def down(self, response):
        item = Acfun_Item()
        req = json.loads(response.text)
        commentsMap = req["commentsMap"]
        for data in commentsMap:
            user_name = commentsMap[data]["userName"]
            content = commentsMap[data]["content"]
            print(content)
            postDate = commentsMap[data]["postDate"]
            if user_name == "去无的止境":
                print("评论:", response.meta['url'], content)
                item["title"] = response.meta['title']
                item["page"] = response.meta['page']
                item["content"] = content
                item["url"] = response.meta['url']
                item["date"] = postDate
                yield item
