#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import json

import os
import requests

class Spider:
    def __init__(self):
        self.session = requests.Session()  #发送http请求

    def run(self,word):
        self.search(word)

    def search(self, word):
        url = 'http://fanyi.baidu.com/v2transapi'
        data = {
            'from': 'en',
            'to': 'zh',
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': 3
        }

        response = self.session.post(url,data)
        info = json.loads(response.text)['dict_result']['simple_means']['symbols'][0]
        # print (info)
        save_info = [word]
        save_info.append('英 [%s] 美 [%s]' %(info['ph_en'], info['ph_am']))
        for part in info['parts']:
            save_info.append("%s %s" % (part['part'],';'.join(part['means'])))
        # print(save_info)
        save_info = ['%s\n' % x for x in save_info]  #列表生成式换行
        self.save(save_info,word)

    def save(self, save_info, word):
        if not os.path.exists(word):
            os.makedirs(word)
        file_path = os.path.join(word,'%s.txt'% word)
        with open(file_path,'w',encoding='utf-8') as f:
            f.writelines(save_info)

if __name__ == '__main__':
    spider = Spider()
    spider.run('find')


