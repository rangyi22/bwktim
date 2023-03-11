#py08e01.py
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10,0.1) # x-축 범위
plt.subplot(2,3,1) # 그림 8.5(a)
y = 0.1*x + 0.3
plt.plot(x,y, 'r')
# x에 대한 0.9*y와 1.1*y의 그래프 사이를 채워주기 위해
plt.fill_between(x, 0.9*y,1.1*y, alpha=0.2) # alpha: 색깔의 농담 
plt.ylim(0,2)  # y-축의 하한/상한을 0/2로 설정 
plt.subplot(2,3,2) # 그림 8.5(b)
y1 = 2 - 0.15*x
# y<y1인 x-축 구간에 대해 y 와 y1 그래프들 사이를 청색으로 
plt.fill_between(x, y,y1, where=(y<y1), color='blue', alpha=0.1)
# y>y1인 x-축 구간에 대해 y 와 y1 그래프들 사이를 적색으로
plt.fill_between(x, y,y1, where=(y>y1), color='red', alpha=0.1)
plt.ylim(0,2)  # y-축 하한과 상한 Setting the y-limit
plt.subplot(2,3,3) # 그림 8.5(c)
plt.plot(x,y,':', label='y=0.1x+0.3')
plt.plot(x,y1,':', label='y1=2-0.15x')
y2 = np.minimum(y,y1)
# x에 대한 y2의 그래프와 0(x-축)사이를 채우기 위해 
plt.fill_between(x, y2, color='green', alpha=0.1)
# plt.fill_between(x, y2,0, color='green', alpha=0.1)
plt.ylim(0,2)  # y-축 범위 설정
plt.legend()
plt.show()
