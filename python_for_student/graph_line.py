#graph_line.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True)
x = [6.1, 5.8, 5.7, 5.6 ,5.5, 5.9, 5.3, 5.2] # Unemployment_Rate
y = [1500,1520,1525,1540,1545,1508,1560,1555] # Stock_Index_Price
plt.subplot(1,2,1)
plt.plot(x,y,'r', x,y,'b.') # 그림 8.3(a)
plt.xlabel('Unemployment Rate', fontsize=10)
plt.ylabel('Stock Index Price', fontsize=10)
plt.title('Unemployment Rate vs. Stock Index Price', fontsize=10)
plt.subplot(1,2,2)
xa = np.array(x);  ya = np.array(y);
sorted_ind = np.argsort(xa) # xa(정렬된 x)의 index들
xa = xa[sorted_ind];   ya = ya[sorted_ind]
plt.plot(xa,ya,'b') # 그림 8.3(b)
plt.xlabel('Unemployment Rate', fontsize=10)
plt.ylabel('Stock Index Price', fontsize=10)
plt.title('Unemployment Rate vs. Stock Index Price', fontsize=10)
plt.show()
