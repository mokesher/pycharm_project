# -*-coding: utf-8 -*-
import pymysql
from collections import Counter

conn = pymysql.connect(host="localhost", user="root", password="root", database="spider", charset="utf8")
cursor = conn.cursor()
cursor.execute("show tables")
table_list = cursor.fetchall()
table_list = [i[0] for i in table_list]
table_list.remove('acfun')

sum = []
for name in table_list:

    sql = '''
    select name,href from {}
    '''.format(name)

    cursor.execute(sql)
    d = cursor.fetchall()

    for item in d:
        sum.append(item[0])

print(Counter(sum))



