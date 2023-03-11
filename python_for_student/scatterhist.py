def scatterhist(x, y, bs_x=None, bs_y=None, Nbs=None):
  import matplotlib.pyplot as plt 
  import numpy as np
  
  if bs_x==None: bs_x=[min(x),max(x)] #Left/Right limits of graph
  if bs_y==None: bs_y=[min(y),max(y)] # Top/Down limits of graph
  if Nbs==None: Nbs = [10, 10] # 두 histogram의 구간(bin) 수
  #각 histogram의 구간(bin) 수, 폭, 경계점들을 만든다.
  Nb_x = Nbs[0];  Nb_y = Nbs[1] # 각 histogram의 구간(bin) 수
  bw_x = (bs_x[1]-bs_x[0])/Nb_x # x-축상의 구간(bin)폭
  bw_y = (bs_y[1]-bs_y[0])/Nb_y # y-축상의 구간(bin)폭
  bins_x = np.arange(bs_x[0], bs_x[1]+bw_x, bw_x) # x-축상 경계점들
  bins_y = np.arange(bs_y[0], bs_y[1]+bw_y, bw_y) # y-축상 경계점들
  # Scatter plot을 그려넣을 사각형의 왼쪽끝, 폭, 아래쪽끝, 높이
  left, width, bottom, height = 0.1, 0.65, 0.05, 0.65
  spacing = 0.02 # Scatter plot과 histogram들간의 간격
  # scatter plot과 두 개의 histogram이 그려질 사각형의 좌하귀, 폭, 높이 
  rect_scatter = [left, bottom, width, height]
  rect_histx = [left, bottom+height+spacing, width, 0.2]
  rect_histy = [left+width+spacing, bottom, 0.2, height]
  fig = plt.figure(figsize=(4, 4)) 
  # scatter plot과 두 개의 histogram이 그려질 사각형 영역과 축을 그린다.   
  ax_scatter = plt.axes(rect_scatter)
  ax_scatter.tick_params(direction='in', top=True, right=True)
  ax_histx = plt.axes(rect_histx)
  ax_histx.tick_params(direction='in', labelbottom=False)
  ax_histy = plt.axes(rect_histy)
  ax_histy.tick_params(direction='in', labelleft=False)
  # Scatter plot
  ax_scatter.scatter(x, y, marker='x', s=5) # Marker style, size
  ax_scatter.set_xlim(bs_x)
  ax_scatter.set_ylim(bs_y)
  # scatter graph의 위/오른쪽에 x/y에 대한 histogram
  ax_histx.hist(x, bins=bins_x)
  ax_histy.hist(y, bins=bins_y, orientation='horizontal')
  ax_histx.set_xlim(ax_scatter.get_xlim())
  ax_histy.set_ylim(ax_scatter.get_ylim())
  plt.show()
