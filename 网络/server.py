#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import socket
import json
 
address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(5)
while True:
    print("waiting for connection...")
    json_string,addr=s.accept()
    print("...connected from:",addr)
    while True:
        data = json_string.recv(2048)
        if (len(data)>0):
            print("Receive '%s'"%data)
            continue
        else:
            break
    json_string.close()
s.close()
