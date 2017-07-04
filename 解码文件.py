#coding=utf-8
import struct
from openpyxl import Workbook
file=open(r'E:\data\GIS数据\网络优化\Heights\changshashi5m.bin','rb')
tuple1=()
x=707830
y=3123840
wb=Workbook() #打开execl表
sheet=wb.active # 抓取活动工作表
for i in range(1,61401):
    data_id=struct.unpack('h',file.read(2))
    file.seek(2*i+1)    
    tuple1+=data_id    
    sheet["C%d"%i].value=tuple1[i-1]    
for n,element1 in enumerate(range(1,212)): #记录循环次数
    for i,element in enumerate(range(1,292)):
        sheet["A%d"%(element+291*(element1-1))].value=x+5*(i%398)+2.5
        sheet["B%d"%(element+291*(element1-1))].value=y+5*(n%348)-2.5
wb.save('E:\data\GIS数据\网络优化\Heights\changshashi5m.xlsx')
    


