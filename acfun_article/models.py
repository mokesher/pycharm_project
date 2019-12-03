#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql


def tosql(*args):
    conn = pymysql.connect(host="localhost", user="root",password="root",database="spider",charset="utf8")
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    result = cursor.execute("SELECT content from acfun WHERE content=%s;",[args[2]])
    if not result:
        cursor.execute("insert into acfun(article_title,page,content,url,date) values(%s,%s,%s,%s,%s)", [*args])
        conn.commit()

    cursor.close()
    conn.close()