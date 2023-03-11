#graph_errorbar.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True)
x = np.arange(0.1, 4, 0.5) # 가상적 data
y = 1-np.exp(-x)
xe = 0.1+0.5*np.log10(1+x) # x에 대한 오차 한계(Error bound)
ye = 0.1*np.sqrt(y)  # y에 대한 오차 한계(Error bound)
plt.subplot(1,3,1)
plt.errorbar(x, y, yerr=ye) 
plt.title('Vertical errorbar plot', fontsize=10) # 그림 8.15(a)
plt.subplot(1,3,2)
plt.errorbar(x, y, xerr=xe, errorevery=(1,2)) # 제1 샘플부터 2개마다
plt.title('Horizontal errorbar plot', fontsize=10) # 그림 8.15(b)
plt.subplot(1,3,3)
plt.errorbar(x, y, yerr=ye, xerr=xe, errorevery=(2,4), fmt='o--') 
plt.title('Vertical/Horizontal errorbar plot', fontsize=10) #그림 (c)
plt.grid()  # errorevery=(2,4), fmt: Format specifier
plt.show()
