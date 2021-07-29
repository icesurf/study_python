# 实时记录数据
import time as t  #引入时间
import smbus2 as smbus  #引入smbus 库 用于adc采集
import xlwt       #引入excel读写库
import xlrd
import numpy as np  #引入numpy数学库
 
time_int = 0.5   #设定采集时间间隔
time_m = 3     #设定采集总时间
timeend =int(time_m*60/time_int)  #循环终止步数
ADC = smbus.SMBus(1)   #adc采集必备
print("数据开始记录")
 
#首先将采集 并需要保存的电压值设定为空集
U1=[]
U2=[]
U3=[]
U4=[]
U5=[]
U6=[]
U7=[]
U8=[]
timeline=[] #时间值
 
 
for i in range(0, timeend):  #进行循环采集
    U1.append( ADC.read_word_data(0x04, 0x10) * 5 / 4096)  # adc通道1 测量值 单位为V
    U2.append( ADC.read_word_data(0x04, 0x11) * 5 / 4096) # adc通道2 测量值
    U3.append( ADC.read_word_data(0x04, 0x12) * 5 / 4096)  # adc通道3 测量值
    U4.append( ADC.read_word_data(0x04, 0x13) * 5 / 4096)  # adc通道4 测量值
    U5.append( ADC.read_word_data(0x04, 0x14) * 5 / 4096)  # adc通道5 测量值
    U6.append( ADC.read_word_data(0x04, 0x15) * 5 / 4096)  # adc通道6 测量值
    U7.append( ADC.read_word_data(0x04, 0x16) * 5 / 4096)  # adc通道7 测量值
    U8.append( (ADC.read_word_data(0x04, 0x17) * 5 / 4096)  # adc通道8 测量值
    t.sleep(time_int)  #时间间隔
    timeline.append((i+1) * time_int) #记录时刻
     #时刻输出保留两位小数的采集值  
    print("%0.2f" % timeline[-1],"%0.2f" % U1[-1] ,"%0.2f" % U2[-1] ,"%0.2f" % U3[-1] ,"%0.2f" % U4[-1] ,"%0.2f" % U5[-1] ,"%0.2f" % U6[-1] ,"%0.2f" % U7[-1] ,"%0.2f" % U8[-1] )
#将数据合成一个矩阵
a = np.array([timeline,U1,U2,U3,U4,U5,U6,U7,filtedData])
f = xlwt.Workbook() # 创建工作簿
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) # 创建sheet
row0 = [u'time',u'U1',u'U2',u'U3',u'U4',u'U5',u'U6',u'U7',u'U8']
 
Uall=a.T #对矩阵进行转置
 
#顺序写入excel表格中
for i in range(0,len(Uall)):
    for j in range(0,len(row0)):
        sheet1.write(i,j,Uall[i,j])
       
f.save('demo.xlsx') #保存为excel文件
————————————————
版权声明：本文为CSDN博主「张渤」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/zhangbochn/article/details/112003825
