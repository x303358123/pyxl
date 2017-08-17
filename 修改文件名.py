#coding=utf-8
import os
import os.path
file = []
for root,dirs,files in os.walk('E:\data\HGHG-NEWOBJ'):
	if files!=[]:
		for file1 in files:
			name,end = os.path.splitext(file1)
			file.append(name)
for name1 in file:
	aa = name1.split('_')
	for root, dirs, files in os.walk('E:\data\HGHG-NEWOBJ'):
		for dirs1 in dirs:
			if dirs1 == aa[1]:
				root1 = os.path.join(root,dirs1)
				root2 = os.path.join(root,aa)
				os.rename(root, root2)