#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
from selenium import webdriver

# chrome = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
# os.environ["webdriver.chrome.driver"] = chrome
# driver = webdriver.Chrome(chrome)
chrome = os.path.abspath(r"chrome")
os.environ["webdriver.chrome.driver"] = chrome
driver = webdriver.Chrome(chrome)

driver.get("https://www.baidu.com")
driver.find_element_by_link_text("登陆").click()

# driver.get("https://www.taobao.com")
# if driver.find_element_by_link_text("亲，请登录"):
#     driver.find_element_by_link_text("亲，请登录").click()
# if driver.find_element_by_link_text("密码登录"):
#     driver.find_element_by_link_text("密码登录").click()
