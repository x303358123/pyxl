#coding=utf-8
import pymysql
import os
import os.path
filename=[]
filename1=[]
b=[]
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
            continue
db=pymysql.connect(host="localhost",port = 3306,user="root",db="changshou",passwd="xialong",charset="utf8")
cur=db.cursor()
cur.execute("""
create table if not EXISTS filename
(
  userid int(11) PRIMARY KEY ,
  drc varchar(50),
  jpg varchar(50)  
)
""")
for i in range(len(b)):
    cur.execute("insert into filename(userid,drc,jpg)values('%d','%s','%s')"%(int(i),str(b[i][0]),str(b[i][1])))
db.commit()
cur.close()
db.close()
