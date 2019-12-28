# _*_coding:utf-8_*_
from selenium import webdriver
import datetime
import time


driver = webdriver.Chrome()
driver.maximize_window()


def login(uname, pwd,url):
    driver.get(url)
    time.sleep(0.5)
    driver.find_element_by_id("username").send_keys(uname)
    driver.find_element_by_id("pwd").send_keys(pwd)
    driver.find_element_by_link_text("登 录").click()

    now = datetime.datetime.now()
    print('login success:',now.strftime('%Y-%m-%d %H:%M:%S'))


def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                try:
                    driver.find_element_by_link_text("发起抢券").click()
                except Exception as e:
                    time.sleep(0.1)
            print ('purchase success',now.strftime('%Y-%m-%d %H:%M:%S'))
            time.sleep(0.5)


# entrance
url = "https://coupon-center.jd.com/skinCoupons.html?#/?activityId=3c3b36b5-c595-447e-9957-0c14d14ebad8&couponId=356c9992-ad15-44fd-b881-bebe7ca656d0&ad_od=share&utm_source=androidapp&utm_medium=appshare&utm_campaign=t_335139774&utm_term=QQfriends"

login('13209432307', 'hxmh23weimei',url)
buy_on_time('2019-12-08 00:00:01')
