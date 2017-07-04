#-*-coding:utf-8-*
import os
import os.path
filename=[]
filename1=[]
txt=open('index.txt','a')
rootdir=input('input:')
txt.write("""<?php
	$cars =array(\n""")
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
            txt.write("		array('%s','%s'),"%(drc,jpg)+'\n')                        
            continue
txt.write("""        );
	echo json_encode($cars);
?>""")
txt.close()
os.rename('E:\资源\python 脚本\index.txt','E:\资源\python 脚本\index.php')
            

			
               
       
