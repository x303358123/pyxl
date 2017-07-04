import ccpx
import math
import os
import os.path
import fileinput

rootdir=input('enter:')
result=[]
aar1=[]
def bbox(vertices):

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
		return [maxx,maxy,maxz,minx,miny,minz]

def ccp(names):

	vertices = []
	previous_line = ""
	for line in fileinput.input(names):
		line = previous_line + line
		if line[-2:-1] == '\\':
			previous_line = line[:-2]
			continue
		previous_line = ""
		chunks = line.split(None, 1)
		if len(chunks) > 1:
			chunks = [chunks[0]] + chunks[1].split()
			if chunks[0] == "v" and len(chunks) == 4:
				x = float(chunks[1])
				y = float(chunks[2])
				z = float(chunks[3])
				vertices.append([x, y, z])
	mami = bbox(vertices)
	return mami

def cpccp(aar1, arr2):

	if aar1 == []:
		aar1 = arr2
	if arr2[0] >aar1[0]:
		aar1[0] = arr2[0]
	if arr2[1] > aar1[1]:
		aar1[1] = arr2[1]
	if arr2[2] > aar1[2]:
		aar1[2] = arr2[2]
	if arr2[3] < aar1[3]:
		aar1[3] = arr2[3]
	if arr2[4] < aar1[4]:
		aar1[4] = arr2[4]
	if arr2[5] < aar1[5]:
		aar1[5] = arr2[5]
	return aar1

for root,dirs,files in os.walk(rootdir):
	for f1 in files:
		if f1.endswith('.obj'):
			result.append(os.path.join(root,f1)) # 获取文件名
for name in result:
	mami = ccp(name)
	aar1 = cpccp(aar1,mami)

x1 = aar1[3]
y1 = aar1[4]
z1 = aar1[5]
x2 = aar1[0]
y2 = aar1[1]
z2 = aar1[2]
a = (-z1+z2)/math.sqrt((-x1+x2)**2+(-y1+y2)**2+(-z1+z2)**2)
b = 180 * math.acos(a) / math.pi
if b>45:
	x = -4 * math.sqrt(2) * math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2) / math.sqrt(
		(-x1 + x2) ** 2 + (-y1 + y2) ** 2)
	y = x
	z = -4 * math.sqrt(2) * math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2)
elif a<30:
	x = -4 * math.sqrt(3) * math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2) / math.sqrt(
		(-x1 + x2) ** 2 + (-y1 + y2) ** 2)
	y = x
	z = -4 * math.sqrt(3) * math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2)
else:
	x = -8 * (-z1+z2)/math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2)
	y = x
	z = 8 * ((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2) / math.sqrt(
		(-x1 + x2) ** 2 + (-y1 + y2) ** 2) * math.sqrt(
		1 - (-z1 + z2) ** 2 / math.sqrt((-x1 + x2) ** 2 + (-y1 + y2) ** 2 + (-z1 + z2) ** 2))
sd = 8 * math.sqrt(
	(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 2 + 2 * (z1 - z2) ** 2) / ((x1 - x2) ** 2 + (y1 - y2) ** 2)) / 6
print(x,y,z)
print(sd)