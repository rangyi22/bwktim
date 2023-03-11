#pyramid_my.py
import matplotlib.pyplot as plt
import numpy as np

def pyramid(x12, xlabels, labels=['Male','Female']):
   # x12는 각 row에 data를 가진 2-row nparray
   x1 = x12[0]; x2=x12[1]
   ys = np.arange(len(xlabels))
   x2_ = np.multiply(x2,-1) # x2에 속한 수의 부호를 minus로 
   max1 = max(x1); max2 = max(x2)
   xd = xd_tick(max(max1,max2)) # 적절한 눈금 간격
   ns1 = np.arange(0,max1,xd) # x1에 대한 눈금
   ns2 = np.arange(xd,max2,xd) # x2에 대한 눈금
   # x2에 대한 눈금값들의 부호를 minus로 만들어서 x1에 대한 눈금과 결합한다. 
   ns = list(np.multiply(ns2,-1)) + list(ns1)
   ns.sort()
   nlabels = list(map(str,np.abs(ns)))
   fig = plt.figure(tight_layout=True)
   plt.barh(ys, x1, height=0.5, label=labels[0]) 
   plt.yticks(ticks=ys, labels=xlabels)
   plt.barh(ys, x2_, height=0.5, label=labels[1])
   plt.xticks(ticks=ns, labels=nlabels)
   plt.legend()
   plt.show()
   
def xd_tick(xmax):
   #data에 있는 숫자의 최대치 xmax에 대해 약 3개 눈금을 잡을만한 단위(간격) 
   N=3; # 대략 x-축에 눈금을 몇 개쯤 매길 지
   dmin = pow(10,np.floor(np.log10(xmax/(N+1))))
   return int(np.ceil(xmax/(N+1)/dmin)*dmin)

male=[15469, 14698, 12956, 11978, 9653, 9137]
female=[16798, 15401, 13467, 12587, 11738, 10614]
years=['14','15', '16','17', '18', '19']
x12 = np.array([male,female])
pyramid(x12, years, ['Male','Female']) # 그림 8.9
