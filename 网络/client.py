#!/usr/bin/env python
# -*- coding: UTF-8 -*-
 
import socket
import json
import os
import os.path
filename=[]
filename1=[]
b=[]
address = ('127.0.0.1', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
rootdir=input('input:')
for root,dirs,files in os.walk(rootdir):
    if files!=[]:        
        for file in files:
            if file.endswith('.drc'):
                filename.append(file)
            if file.endswith('.jpg'):
                filename1.append(file)
for drc in filename:
    for jpg in filename1:
        if drc[0:-4]==jpg[0:-6]:
            a=[]            
            a.append(drc)
            a.append(jpg)
            b.append(a)
            
mylist = b
json_string = json.dumps(mylist)
bjson_string=bytes(json_string,encoding='utf-8')
s.send(bjson_string)
s.close()
