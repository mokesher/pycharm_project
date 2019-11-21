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
            elif ".mp4" in i:
                print(file)
                try:
                    shutil.move(file, result_file)
                except shutil.Error:
                    name = i.rsplit(".")[0]
                    typ = i.rsplit(".")[-1]
                    new_name = name + str(random.randint(0,99)) + "." + typ
                    print("rename",new_name)
                    new_file = os.path.join(start_path,new_name)
                    os.rename(file, new_file)
                    shutil.move(new_file, result_file)
        else:
            run(file, result_file)


start_path = r"E:\wanru35t"
result_file = start_path
run(start_path, result_file)


