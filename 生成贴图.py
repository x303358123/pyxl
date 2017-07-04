# -*- coding: UTF-8 -*-
import pymysql
from PIL import Image
file=[]
db=pymysql.connect(host="10.10.1.109",port = 3306,user="root",db="changsha",passwd="Newdatar@2017",charset="utf8")
cur=db.cursor()
aa=cur.execute("SELECT * FROM coverface_max_46")
f=cur.fetchmany(aa)
for d in f:
    file.append(d[12])
cur.close()
db.close()
x = 256 #x坐标  通过对txt里的行数进行整数分解
y = 256 #y坐标  x*y = 行数

im = Image.new("RGB",(x,y))#创建图片

#通过一个个rgb点生成图片
for j in range(0,x):
    for i in range(0,256):
        if aa<256*j+i+1:
            break
        line = file[256*j+i] #获取一行
        rgb = line.split(",") #分离rgb
        if rgb[0]=='':
            r=150
            g=150
            b=150
        else:
            r=float(rgb[0])*255
            g=float(rgb[1])*255
            b=float(rgb[2])*255
        im.putpixel((i,j),(int(r),int(g),int(b)))#rgb转化为像素

im.save('coverface_max_46.png')
