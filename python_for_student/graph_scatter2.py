#graph_scatter2.py
import matplotlib.pyplot as plt

# Given data
x1 = [3, 3.5, 3.7, 4, 4.5, 5, 5.2]  # Low income
y1 = [8, 8.5, 9, 9.5, 10, 10.5, 11] # Savings
x2 = [7.5, 8, 8.5, 9, 9.5, 10, 10.5] # High income
y2 = [1, 1.5, 2, 2.5, 3, 3.5, 3.6]  # Savings
datas = ((x1, y1), (x2, y2))  # 두 group에 대한 data
colors = ('blue', 'red')       # 두 group에 대한 색깔
labels = ('Low income', 'High income') # 두 group에 대한 label
for i, data in enumerate(datas):
   x, y = data;  color = colors[i]; label = labels[i]   
   plt.scatter(x, y, s=8, c=color, alpha=0.8, label=label)
plt.title('Income vs. Saving', fontsize=10)
plt.xlabel('Income')
plt.ylabel('Saving')
plt.legend(loc=1) # legend를 우상귀(upper right corner)에 위치시킨다.
plt.show()
