#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from wordcloud import WordCloud,get_single_color_func,ImageColorGenerator
import matplotlib.pyplot as plt
import jieba

myword = []
text = open(r"C:\Users\MOKE\Desktop\word.txt",encoding="utf-8").read()

seg_list = jieba.cut(text,cut_all=False)
liststr = "/".join(seg_list)
for word in liststr.split("/"):
	if len(word.strip())>1:
		myword.append(word)
print(myword)
text = ' '.join(str(i) for i in myword)

wordcloud = WordCloud(background_color="white",random_state=42,max_words=400,max_font_size=220,height=1500,width=1560,font_path=".\simkai.ttf",margin=2).generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("test.png")
print("OK")
