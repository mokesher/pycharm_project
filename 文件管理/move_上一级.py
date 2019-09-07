#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os,sys,shutil,random

file_path = r"path"

for i in os.listdir(file_path):
    each_dir = os.path.join(file_path,i)
    if os.path.isdir(each_dir):
        for j in os.listdir(each_dir):
            file = os.path.join(each_dir, j)
            print(file)
            try:
                shutil.move(file, file_path)
            except:
                num = str(random.randint(1, 99))
                new = j.rsplit(".", 1)[0] + num + "." + j.rsplit(".", 1)[1]
                new_file = os.path.join(each_dir, new)
                os.rename(file, new_file)
                shutil.move(new_file, file_path)

