import os
import os.path
import csv
rootdir=input('enter:')
obj=[]
mtl=[]
png=[]
jpg=[]
vertices=[]
files=open('E:\资源\obj\data.csv','w+')
previous_line=""
for root,dirs,files in os.walk(rootdir):
    for f1 in files:
        if f1.endswith('.obj'):
            obj.append(os.path.join(root,f1))
        elif f1.endswith('.mtl'):
            mtl.append(os.path.join(root,f1))            
        elif f1.endswith('.png'):
            png.append(os.path.join(root,f1))            
        elif f1.endswith('.jpg'):
            jpg.append(os.path.join(root,f1))            
for i in range(len(obj)):
    if png==[]:
        a1=''.join(obj[i]+','+mtl[i]+','+jpg[i])
        print(a1,file=files)
    else:
        a1=''.join(obj[i]+','+mtl[i]+','+jpg[i])
        print(a1,file=files)
files.close()

        
