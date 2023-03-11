#graph_ticker_format.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

fig = plt.figure(tight_layout=True)
plt.subplot(1,2,1)
x = np.linspace(1, 20, 101)
y = np.exp(x)
plt.plot(x, y)
ax1 = plt.gca()
xlabels = ax1.get_xticks()
ax1.set_xticklabels([f'{x:.1f}' for x in list(xlabels)])
ylabels = ax1.get_yticks()
#ylabels=ylabels[ylabels>0] # 만약 log값 눈금을 위해 +값만 취하려면
ax1.set_yticklabels([f'{y:.1e}' for y in ylabels])
ax2 = plt.subplot(1,2,2)
ax2.plot(x, y)
ax2.set_yscale('log')
ax2.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.1f'))
ax2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%.1e'))
plt.show()
