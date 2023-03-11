#graph_pyramid.py
import matplotlib.pyplot as plt
import numpy as np

years=['14','15', '16','17', '18', '19'] 
x = np.arange(len(years))
male=[15469, 14698, 12956, 11978, 9653, 9137]
female=[16798, 15401, 13467, 12587, 11738, 10614]
fig, axs = plt.subplots(ncols=2, sharey=True, tight_layout=True)
axs[0].barh(x, male, height=0.5)
axs[0].set(title='Male')
axs[0].invert_xaxis()
axs[0].set(yticks=x, yticklabels=years) # 부록 G의 표 G.2 참조
axs[0].yaxis.tick_right()
axs[1].barh(x, female, height=0.5) 
axs[1].set(title='Female')
plt.show()
