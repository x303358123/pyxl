#-*-coding:utf-8-*
# jpg obj mtl存放在一个文件夹内
import os
import os.path
import shutil
filename=[]
rootdir=input('input:')
rootex=input('export:')
for root,dirs,files in os.walk(rootdir):
    if files!=[]:        
        for file in files:
            if file.endswith('.obj'):
                wenj,houz=os.path.splitext(file)
                filename.append(wenj)
                b=os.listdir(rootex) #返回目录下文件名
                if wenj[15:18] not in b:
                    # 创建上级文件目录
                    os.mkdir(os.path.join(rootex,wenj[15:18]))
                else:
                    continue
for c in filename:		
	if c not in b:
		os.mkdir(os.path.join(rootex,c)) #创建文件目录
	else:
		continue
for root1,dirs1,files1 in os.walk(rootdir):
    if files1!=[]:
        for file1 in files1:
            if len(file1)>20:                
                wenj1,houz1=os.path.splitext(file1)
                shutil.copy(os.path.join(root1,file1),os.path.join(rootex,wenj1[:18]))
b=os.listdir(rootex)
for newdirs in b:    
    if len(newdirs)>5:
        # 移动文件夹
        shutil.move(os.path.join(rootex,newdirs),os.path.join(rootex,newdirs[15:18]))        
    else:
        continue
            
    

                
            
        
    
