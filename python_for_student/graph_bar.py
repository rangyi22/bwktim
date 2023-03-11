#graph_bar.py
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(tight_layout=True)
years=['14','15', '16','17', '18', '19'] 
x = np.arange(len(years))
male=[154697, 146983, 129564, 119782, 96539, 91374]
female=[167981, 154012, 134675, 125879, 117386, 106143]
plt.subplot(2,2,1)
plt.bar(x, male, width=0.2)
plt.xticks(x, years)  # 그림 8.7(a)
plt.subplot(2,2,2)
plt.bar(x-0.1, male, width=0.2)  # 그림 8.7(b)
plt.bar(x+0.1, female, width=0.2)
plt.xticks(x, years)
plt.subplot(2,2,3)
plt.barh(x, male, height=0.5, color='red')  # 그림 8.7(c)
plt.barh(x, female, height=0.5, left=male, color='blue') 
plt.yticks(x, years)
plt.subplot(2,2,4)  # 그림 8.7(d)
plt.bar(x, male, width=0.5, color='red') 
plt.bar(x, female,width=0.5, bottom=male, color='blue')
plt.xticks(x, years)
plt.show()
