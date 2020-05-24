#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 8001))
sk.listen()

while 1:
    conn, addr = sk.accept()
    data = conn.recv(8096)
    conn.send(b'http/1.1 200 OK\r\n\r\n')
    print(data)
    conn.send(b"hello world")
    conn.close()
    sk.close()
