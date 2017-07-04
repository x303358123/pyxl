#-*-coding:utf-8-*

import os
import os.path
import ccpx

def filenames(rootdirs,endwith):
	filename = []
	for [root, dirs, files] in os.walk(rootdirs):
		if files!=[]:
			for file in files:
				if file.endswith(endwith):
					wenj,houz=os.path.splitext(file)
					filename.append(wenj)
	return filename

def chname(filename: object) -> object:
	file,endwith = os.path.splitext(filename)
	file1 = file.replace('+','1')
	file2 = file1.replace('-','0')
	aa = file2.split('_')
	aa[3] = aa[3][1:]
	cc = ''.join(aa[1:-1])
	bb = aa[-1]
	return [cc,bb]

drcname=filenames('E:\data\cs-full-lod','drc')
dic = {}
for name in drcname:
	if len(name)>18:
		cname = chname(name)
		# 字典添加值
		if cname[0] not in dic.keys():
			dic[cname[0]] = [cname[1]]
		else:
			dic[cname[0]].append(cname[1])

files = open('level.txt','a')
files.truncate(0) #删除文件内容
k = sorted(dic.keys()) # key值排序
for key in k:
	st = ','.join(dic[key])
	files.write('[1/'+key[0]+'/'+key[1:4]+'/'+key[4]+'/'+key[5:8]+'/'+key+'/'+key[8:]+'/ture/false/ture/0'+'/'+st+']\n')
files.close()
fileo = open('ccp.txt','a')
fileo.truncate(0)  #删除文件内容
for [root, dirs, files] in os.walk('E:\data\cs-full-lod'):
	if files != []:
		for file in files:
			if file.endswith('.obj'):
				obj = os.path.join(root,file)
				cc = ccpx.ccp(obj)
				centerx = str((cc[0]+cc[1])/2)
				centery = str((cc[2]+cc[3])/2)
				centerz = str((cc[4]+cc[5])/2)
				ro,fl = os.path.split(obj)
				wj = chname(fl)
				fileo.write(wj[0][:-2]+'/'+centerx+'/'+centery+'/'+centerz+'/0]')
fileo.close()






