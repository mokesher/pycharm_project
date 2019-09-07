#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import hashlib
import socket
import os
server = socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr = server.accept()
    print("new conn:",addr)
    while True:
        print("等待新指令")
        data = conn.recv(1024)
        if not data:
            print("客户端已断开")
            break
        cmd,filename = data.decode().split()       # split : get filename
        print(filename)
        if os.path.isfile(filename):               # 传输的是一个文件
            f = open(filename,'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size  #文件大小
            conn.send( str(file_size).encode() )   #发送大小
            conn.recv(1024)
            for line in f:
                # m.update(line)
                conn.send(line)
            # print("file md5",m.hexdigest())
            f.close()

        print("send done")

server.close()