# -*- coding:utf-8 -*-
import os, shutil, random

file_list = (".wmv", ".mp4", ".mkv", ".avi", ".mov")

def run(start_path, result_file):
    path_list = os.listdir(start_path)
    for i in path_list:
        file = os.path.join(start_path, i)
        if os.path.isfile(file):
            if file == os.path.join(result_file, i):
                continue
            elif i.lower().endswith(file_list):
                print(file)
                try:
                    shutil.move(file, result_file)
                except shutil.Error:
                    name = i.rsplit(".")[0]
                    type = i.rsplit(".")[-1]
                    new_name = f"{name}-{random.randint(0, 999)}.{type}"
                    print("rename", new_name)
                    new_file = os.path.join(start_path, new_name)
                    os.rename(file, new_file)
                    shutil.move(new_file, result_file)
        else:
            run(file, result_file)


start_path = r"D:\迅雷下载"
result_file = start_path
run(start_path, result_file)
