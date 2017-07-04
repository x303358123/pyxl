#coding=utf-8
import pymysql
import math

db=pymysql.connect(host="10.10.1.114",port = 3306,user="root",db="user",passwd="123456",charset="utf8")
cur=db.cursor()
aa=cur.execute("select * from coverface_max_final")
info=cur.fetchmany(aa)
file=open('coverface.txt','a')
file.truncate(0)
file.write('mtllib building.mtl\n')
for e,i in enumerate(info): # 记录循环次数
    x=float(i[8])
    y=float(i[9])
    z=float(i[10])
    file.write('v'+' '+str(x-2.5)+' '+str(y-2.5)+' '+str(z-2.5)+'\n')
    file.write('v'+' '+str(x+2.5)+' '+str(y-2.5)+' '+str(z-2.5)+'\n')
    file.write('v'+' '+str(x+2.5)+' '+str(y+2.5)+' '+str(z-2.5)+'\n')
    file.write('v'+' '+str(x-2.5)+' '+str(y+2.5)+' '+str(z-2.5)+'\n')
    file.write('v'+' '+str(x-2.5)+' '+str(y-2.5)+' '+str(z+2.5)+'\n')
    file.write('v'+' '+str(x+2.5)+' '+str(y-2.5)+' '+str(z+2.5)+'\n')
    file.write('v'+' '+str(x+2.5)+' '+str(y+2.5)+' '+str(z+2.5)+'\n')
    file.write('v'+' '+str(x-2.5)+' '+str(y+2.5)+' '+str(z+2.5)+'\n')
file.close()
cur.close()
db.commit()
db.close()

file=open('coverface.txt','a')
file.truncate(0)
for k in range(1,math.ceil(e/256+1)):
    for j in range(1,257):    
        file.write('vt'+' '+str((2*j-1)/512)+' '+str(1-(2*k-1)/512)+'\n')
for l in range(0,e+1):
    a=[2+8*l,1+8*l,4+8*l,3+8*l]
    b=[6+8*l,5+8*l,8+8*l,7+8*l]
    file.write('f'+' '+str(a[2])+'/'+str(l+1)+' '+str(a[3])+'/'+str(l+1)+' '+str(a[0])+'/'+str(l+1)+' '+str(a[1])+'/'+str(l+1)+'\n')
    file.write('f'+' '+str(b[1])+'/'+str(l+1)+' '+str(b[0])+'/'+str(l+1)+' '+str(b[3])+'/'+str(l+1)+' '+str(b[2])+'/'+str(l+1)+'\n')
    file.write('f'+' '+str(b[0])+'/'+str(l+1)+' '+str(b[1])+'/'+str(l+1)+' '+str(a[1])+'/'+str(l+1)+' '+str(a[0])+'/'+str(l+1)+'\n')
    file.write('f'+' '+str(b[1])+'/'+str(l+1)+' '+str(b[2])+'/'+str(l+1)+' '+str(a[2])+'/'+str(l+1)+' '+str(a[1])+'/'+str(l+1)+'\n')
    file.write('f'+' '+str(b[2])+'/'+str(l+1)+' '+str(b[3])+'/'+str(l+1)+' '+str(a[3])+'/'+str(l+1)+' '+str(a[2])+'/'+str(l+1)+'\n')
    file.write('f'+' '+str(b[3])+'/'+str(l+1)+' '+str(b[0])+'/'+str(l+1)+' '+str(a[0])+'/'+str(l+1)+' '+str(a[3])+'/'+str(l+1)+'\n')
file.close()

