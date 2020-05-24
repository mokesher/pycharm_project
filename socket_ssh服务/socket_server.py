#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import socket, os

server = socket.socket()
server.bind(('localhost', 9999))
server.listen()  # decode   encode
#   bytes>>str>>bytes
while True:
    conn, addr = server.accept()
    print("new conn:", addr)
    while True:
        data = conn.recv(1024)  # data bytes类型 大小官方建议不超过8k(8192)
        if not data:
            print("客户端已断开")
            break
        print("执行指令:", data.decode())
        cmd_res = os.popen(data.decode()).read()  # 接收到bytes数据解码为os.popen需要的str，接受字符串，执行结果也为字符串
        if len(cmd_res) == 0:
            cmd_res = "cmd has no ouput"
        conn.send(str(len(cmd_res.encode())).encode("utf-8"))  # send（中文字符len判断长度需要encode>bytes一个中文为3个字节）
        client_ack = conn.recv(1024)
        print("ack from client", client_ack.decode())
        conn.send(cmd_res.encode("utf-8"))  # send bytes类型数据，encode>>  bytes(只能是英文ASCII)

server.close()
