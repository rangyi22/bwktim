#graph_stack.py
import matplotlib.pyplot as plt
years = [1960, 1980, 2000, 2020]
children = [10587583, 12950775, 9911229, 6118611]
working = [13698341, 23716967, 33701986, 35506403]
seniors = [726450, 1456033, 3394896, 7701125]
plt.plot([],[], color='m', linewidth=5, label='Children')
plt.plot([],[], color='c', linewidth=5, label='Working')
plt.plot([],[], color='r', linewidth=5, label='Seniors')
plt.stackplot(years, children, working, seniors, colors='mcr')
plt.xlabel('Year');  plt.ylabel('Population')
plt.title('Stack Plot', fontsize=10)
plt.legend(loc='upper left')
plt.show()
