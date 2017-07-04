#-*-coding:utf-8-*
# jpg文件存放在image
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
                b=os.listdir(rootex) #返回目录内文件名
                if wenj[15:18] not in b and wenj[15:18]!='':   
                    os.makedirs(os.path.join(os.path.join(rootex,wenj[15:18]),'image'))   # 创建上级文件目录                 
                else:
                    continue
for root1,dirs1,files1 in os.walk(rootdir):
    if files1!=[]:
        for file1 in files1:
            if len(file1)>20:                
                if file1.endswith('.jpg'):  # jpg文件存储
                    wenj1,houz1=os.path.splitext(file1)
                    shutil.copy(os.path.join(root1,file1),os.path.join(rootex,wenj1[15:18],'image'))
                else:
                    wenj1,houz1=os.path.splitext(file1) # obj mtl文件存储
                    shutil.copy(os.path.join(root1,file1),os.path.join(rootex,wenj1[15:18]))
            else:shutil.copy(os.path.join(root1,file1),rootex)
                    
    


    
        
