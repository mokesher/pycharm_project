#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pymysql


def tosql_fans(name,*args):
    conn = pymysql.connect(host="localhost",user="root",password="root",database="spider",charset="utf8")
    cursor = conn.cursor()
    cursor.execute("show tables")
    data = cursor.fetchall()
    blog = name.lower() + "_fans"
    if (f'{blog}',) not in data:
        sql = '''
        CREATE TABLE {}  (
          id int(11) NOT NULL AUTO_INCREMENT,
          href varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
          name varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
          page int(11) NOT NULL,
          PRIMARY KEY (id) USING BTREE,
          UNIQUE INDEX href(href) USING BTREE
        )
        '''.format(blog)
        cursor.execute(sql)
    else:
        sql = f"select href from {blog} where href=%s"
        result = cursor.execute(sql,args[0])
        if not result:
            sql = f"insert into {blog} (href,name,page) values(%s,%s,%s)"
            cursor.execute(sql, (args))

    conn.commit()
    cursor.close()
    conn.close()


def tosql_follow(name,*args):
    conn = pymysql.connect(host="localhost",user="root",password="root",database="spider",charset="utf8")
    cursor = conn.cursor()
    cursor.execute("show tables")
    data = cursor.fetchall()
    blog = name.lower() + "_follow"
    if (f'{blog}',) not in data:
        sql = '''
        CREATE TABLE {}  (
          id int(11) NOT NULL AUTO_INCREMENT,
          href varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
          name varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
          page int(11) NOT NULL,
          PRIMARY KEY (id) USING BTREE,
          UNIQUE INDEX href(href) USING BTREE
        )
        '''.format(blog)
        cursor.execute(sql)
    else:
        sql = f"select href from {blog} where href=%s"
        result = cursor.execute(sql,args[0])
        if not result:
            sql = f"insert into {blog} (href,name,page) values(%s,%s,%s)"
            cursor.execute(sql, (args))

    conn.commit()
    cursor.close()
    conn.close()

