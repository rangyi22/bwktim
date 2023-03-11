#graph_boxplot.py
import matplotlib.pyplot as plt
# 두 data set
g = [65,67,68,68,68,69,69,69,69,70,70,70,70,70,71,71,71,71.5,74]
g1 = [66,66,67,67,68,68,68,69,69,69,69,70,70,70,70,71,71,71,72,72]
# 두 data set에 대한 수평형(horizontal) boxplot 도시하기
plt.boxplot([g,g1], vert=False, labels=['g','g1']) # 그림 8.14(a)
plt.grid(True)
plt.show()
