#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os,sys,shutil,random


def run(start_path, result_file):
    path_list = os.listdir(start_path)
    for i in path_list:
        file = os.path.join(start_path,i)

        if os.path.isfile(file):
            if file == os.path.join(result_file,i):
                continue
            elif ".avi" in i:

                print(file)
                shutil.move(file, result_file)

        else:
            run(file, result_file)


start_path = r"E:\java\01-JavaSE知识(学习27天)\day06(面向对象-类&private&this)"
result_file = start_path

run(start_path, result_file)


