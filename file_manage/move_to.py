# -*- coding:utf-8 -*-
import os, shutil, random


def run(start_path, result_file):
    path_list = os.listdir(start_path)
    for i in path_list:
        file = os.path.join(start_path, i)
        if os.path.isfile(file):
            if file == os.path.join(result_file, i):
                continue
            elif i.lower().endswith(".wmv") or i.lower().endswith(".mp4")\
                    or i.lower().endswith(".mkv")\
                    or i.lower().endswith(".avi")\
                    or i.lower().endswith(".mov"):
            # elif i.endswith(".flac") or i.endswith(".mp3"):
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


start_path = r"D:\bz"
result_file = start_path
run(start_path, result_file)
