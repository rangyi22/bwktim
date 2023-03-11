#graph_table.py
import matplotlib.pyplot as plt
import numpy as np

data = [[5200, 4900, 3500], # 남한인구수
          [2500, 2400, 2300]] # 북한인구수
행표시 = ['S. Korea', 'N. Korea']
열표시 = ["2019", "2040", "2067"]
x = [1, 2, 3]
Nrow, Ncol = len(data), len(data[0])
colors = plt.cm.BuPu(np.linspace(0.3, 0.9, Nrow)) # 색깔모음
#colors = ['blue', 'red'] # 색깔모음을 이런 식으로 지정할 수도 ..
#colors = colors[::-1] # 색깔의 순서를 거꾸로 하려면
#data.reverse() # data를 세로방향으로 대칭이동하려면 
y_offset = np.zeros(Ncol)
for m in range(Nrow):
    plt.bar(x, data[m], bottom=y_offset, width=0.5, color=colors[m]) 
    y_offset += data[m]
plt.table(cellText=data, colLabels=열표시, rowLabels=행표시, loc='top')
plt.xticks(ticks=x, labels=열표시)
#plt.axis('off') # 축을 제거하려면 맨 앞의 #를 지워서 (uncomment) 활성화시켜
plt.show()
