#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import random
from PIL import Image, ImageFilter, ImageDraw, ImageFont

num = str(random.randint(0, 9))
color = random.randint(0, 255)
im = Image.open('1.jpg')  # 打开一个jgp图片，当前目录
w, h = im.size  # 获取图像尺寸
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 100)
print("original image size: %s %s\n%s" % (w, h, num))
# im.thumbnail((w//2,h//2))                 #缩放%50
im = im.filter(ImageFilter.BLUR)  # 应用模糊滤镜
draw = ImageDraw.Draw(im)
draw.text((9 * w / 10, h / 20), num, font=font, fill=color)

im.show()
im.save("图片/x.png")
