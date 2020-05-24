#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import urllib.parse as parse

res = "http://message.t.qq.com/newMsgCount.php?&type=4%2C2%2C1%2C20%2C19%2C13&r=158967927&source=1&atType=4&apiType=14&apiHost=http%3A%2F%2Fapi.t.qq.com&_r=1589679279777&g_tk=738432772"
print(parse.unquote(res))
