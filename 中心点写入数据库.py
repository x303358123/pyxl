#-*-coding:utf-8-*
import fileinput
import os
import os.path
import pymysql
rootdir=input('enter:')
result=[]
vertices=[]
b=[]
previous_line=""
for root,dirs,files in os.walk(rootdir):
    for f1 in files:
        if f1.endswith('.obj'):
            result.append(os.path.join(root,f1))
            
for name in result:
    for line in fileinput.input(name):        
        dirss,filess=os.path.split(name)
        line=previous_line+line    
        if line[-2:-1]=='\\':
                previous_line =line[:-2]
                continue
        previous_line = ""
        chunks = line.split(None, 1)
        if len(chunks) > 1:
            chunks = [chunks[0]] + chunks[1].split()
            if chunks[0] == "v" and len(chunks) == 4:
                x = float(chunks[1])
                y = float(chunks[2])
                z = float(chunks[3])
                vertices.append([x,y,z])
   
    if len(vertices)>0:
        minx = maxx = vertices[0][0]
        miny = maxy = vertices[0][1]
        minz = maxz = vertices[0][2]
        for v in vertices[1:]:
            if v[0]<minx:
                minx = v[0]
            elif v[0]>maxx:
                maxx = v[0]
            if v[1]<miny:
                miny = v[1]
            elif v[1]>maxy:
                maxy = v[1]
            if v[2]<minz:
                minz = v[2]
            elif v[2]>maxz:
                maxz = v[2]            
        a=[(minx+maxx)/2,(miny+maxy)/2,(minz+maxz)/2]
        a.append(filess)
        b.append(a)
        vertices=[]
        
db=pymysql.connect(host="localhost",port = 3306,user="root",db="changshou",passwd="xialong",charset="utf8")
cur=db.cursor()
cur.execute("""
create table if not EXISTS zhongxing
(
  userid int(11) PRIMARY KEY ,
  obj varchar(50),
  x float,
  y float,
  z float
)
""")
for i in range(len(b)):    
    cur.execute("insert into zhongxing(userid,obj,x,y,z)values('%d','%s',%.6f,%.6f,%.6f)"%(int(i),str(b[i][3]),float(b[i][0]),float(b[i][1]),float(b[i][2])))
db.commit()
cur.close()
db.close()
