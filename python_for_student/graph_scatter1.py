#graph_scatter1.py
import matplotlib.pyplot as plt

#fig=plt.figure(tight_layout=True) # 그래프가 한 개뿐이면 굳이 필요없다.
# 주어진 data
x = [6.1, 5.8, 5.7, 5.6 ,5.5, 5.9, 5.3, 5.2] # 실업률 
y = [1500,1520,1525,1540,1545,1508,1560,1555] # 주가지수
plt.scatter(x, y, s=6, c='blue', alpha=1)
# s: 점의 크기, c: 점의 색깔, alpha: 점 색깔의 진하고 연한 (농담) 정도 0~1
plt.title('Unemployment Rate vs. Stock Index Price', fontsize=10)
plt.xlabel('Unemployment Rate', fontsize=10)
plt.ylabel('Stock Index Price', fontsize=10)
plt.grid(True) # 눈금선(grid lines)
plt.show()
