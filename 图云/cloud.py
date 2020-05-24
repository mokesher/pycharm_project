#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from wordcloud import WordCloud, get_single_color_func, ImageColorGenerator
import matplotlib.pyplot as plt
from PIL import Image
# import jieba,chardet
from word_frequency import word_frequency
import numpy as np

# temp = {}
# for j,k in word_frequency.items():
#     j = unicode(j.decode("utf-8"))
#     temp[j] = k
# print(temp)

myword = []
# text = open(r"word.txt",encoding="utf-8").read()
# text = open(r"word.txt").readlines()
# for i in text:
#     myword.append(i.strip())
# seg_list = jieba.cut(text,cut_all=False)
# liststr = "/".join(seg_list)
# for word in liststr.split("/"):
# 	if len(word.strip())>1:
# 		myword.append(word)
# print(myword)
# text = ' '.join(str(i) for i in myword)

# text = ' '.join(str(i) for i in text)
# print(text)
# text = ' '.join(myword)
# print(text)

image = np.array(Image.open('background/1.jpg'))

wc = WordCloud(
    background_color="white",
    mask=image,
    scale=4,
    random_state=42,
    max_words=800,
    max_font_size=100,
    height=2500,
    width=2560,
    font_path="./simkai.ttf",
    margin=2)

# wordcloud = wc.generate(text)
wc.generate_from_frequencies(word_frequency)
image_colors = ImageColorGenerator(image)
wc.recolor(color_func=image_colors)

plt.imshow(wc)
plt.axis("off")
plt.show()
wc.to_file("test.png")
print("OK")
