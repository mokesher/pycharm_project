# -*- coding:utf-8 -*-
import os,sys,shutil,random

def run(start_path, result_file):

    path_list = os.listdir(start_path)
    for i in path_list:
        file = os.path.join(start_path, i)
        if i == "Need For Speed Heat" and i == "NFS18.Rivals.CHT.Green.Edition-ALI213":
            continue
        if os.path.isfile(file):
            if file == os.path.join(result_file, i):
                continue
            elif i.endswith(".wmv") or i.endswith(".mp4"):
                print(file)
                try:
                    shutil.move(file, result_file)
                    pass
                except shutil.Error:
                    name = i.rsplit(".")[0]
                    type = i.rsplit(".")[-1]
                    new_name = f"{name}-{random.randint(0,99)}.{type}"
                    print("rename", new_name)
                    new_file = os.path.join(start_path,new_name)
                    os.rename(file, new_file)
                    shutil.move(new_file, result_file)
        else:
            run(file, result_file)


start_path = r"E:\新建文件夹"
result_file = start_path
run(start_path, result_file)


