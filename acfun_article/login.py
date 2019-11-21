#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests


def Login():
    url = "https://id.app.acfun.cn/rest/web/login/signin"
    data = {
        "username": "13321270519",
        "password": "hxmh23wei"
            }
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"}

    login_session = requests.session()
    login_response = login_session.post(url,data=data,headers=headers)
    return login_session


if __name__ == "__main__":
    Login()