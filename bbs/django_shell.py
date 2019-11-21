#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")
    import django
    django.setup()

    from blog import models
    from django.db.models import Count
    user = models.UserInfo.objects.filter(username="moke").first()
    # ret = models.Category.objects.filter(blog=user.blog).annotate(c=Count("article")).values()
    # ret = models.Article.objects.filter(user=user).extra(
    #     select={"archive_ym": "date_format(create_time,'%%Y-%%m')"}
    # ).values("archive_ym").annotate(c=Count("nid")).values("c","archive_ym")
    # blog = user.blog
    # article_obj = models.Article.objects.filter(nid=1).first()
    # print(article_obj.ar)
    # article_obj = models.Article.objects.filter(pk=9).values("articledetail__content")
    # ArticleDetail_obj = models.ArticleDetail.objects.filter(pk=2).values("article__desc")
    # printArticleDetail_obj)
    from bs4 import BeautifulSoup
    obj = models.ArticleDetail.objects.filter(pk=1).first().content
    soup = BeautifulSoup(obj,"html.parser")
    print(soup.prettify())







