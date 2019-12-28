# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from scrapy_demo.items import Acfun_qiangan
import json,time,re


class AcfunSpider(scrapy.Spider):
    name = 'acfun'
    allowed_domains = ['acfun.cn']
    start_urls = ['https://webapi.acfun.cn/query/article/list?pageNo=1&size=10&realmIds=25%2C34%2C7%2C6%2C17%2C1%2C2&originalOnly=false&orderType=1&periodType=-1&filterTitleImage=true',
                  "https://webapi.acfun.cn/query/article/list?pageNo=1&size=10&realmIds=5%2C22%2C3%2C4&originalOnly=false&orderType=2&periodType=-1&filterTitleImage=true"
                  ]

    def start_requests(self):
        loginUrl = "https://id.app.acfun.cn/rest/web/login/signin"
        yield scrapy.FormRequest(url=loginUrl,formdata={"username": "13321270519",
                                                         "password": "hxmh23wei", },
                                               callback=self.after_login
                                               )

    def after_login(self, response):
        print("after_login")
        for url in self.start_urls: 
            yield scrapy.Request(url=url,callback=self.article_list)

    def article_list(self, response):
        index_url = response.url
        article_list = json.loads(response.text)['data']['articleList']
        for article in article_list:
            id = article['id']
            comment_count = article["comment_count"]
            article_title = article['title']
            url = "http://www.acfun.cn/v/ac" + str(id)
            total_page = int(comment_count / 50) + 1
            for page in range(1, total_page + 1):
                print("————————page————————:",page)
                req_url = f"https://www.acfun.cn/rest/pc-direct/comment/listByFloor?" \
                          f"sourceId={id}&sourceType=3&page={page}&pivotCommentId=0&" \
                          f"newPivotCommentId=0&_ts={int(100 * time.time())}"

                yield scrapy.Request(req_url,callback=self.get_parse,meta={'article_title': article_title,"url": url,"page": page})

        next_page = "pageNo=" + str(int(re.search(r'pageNo=(\d+)', index_url).group(1)) + 1)
        print(next_page)
        next_url = re.sub(r'pageNo=(\d+)', next_page, index_url)
        yield scrapy.Request(url=next_url, callback=self.article_list)

    def get_parse(self, response):
        item = Acfun_qiangan()
        article_txt = json.loads(response.text)["commentsMap"]
        article_title = response.meta['article_title']
        # print(article_title)
        for data in article_txt:
            user_name = article_txt[data]["userName"]
            if user_name == "Syer_Lu":
                print(article_title)
                item["article_title"] = article_title
                item["page"] = response.meta['page']
                item["content"] = article_txt[data]["content"]
                item["url"] = response.meta['url']
                item["date"] = str(article_txt[data]["postDate"])

                yield item



