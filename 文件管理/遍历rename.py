#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os,shutil


def run(all_path):
    path_list = os.listdir(all_path)
    for i in path_list:
        file = os.path.join(all_path,i)
        if os.path.isfile(file):
            if i.find(" ")>1:
                print(i)
                new_name = i.replace("  ", "")
                new_file = os.path.join(all_path, new_name)
                # print(new_file)
                os.rename(file,new_file)

        else:
            run(file)


all_path = r"file"
run(all_path)


