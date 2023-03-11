#hist3d_my.py
def hist3d_my(x, y, Nb=10, range=None, ax=None):
   # Nb: Number of bins 
   import matplotlib.pyplot as plt
   import numpy as np
   if range==None: range=[[min(x),max(x)],[min(y),max(y)]]
   zs, xs, ys = np.histogram2d(x, y, Nb, range)  
   # 각 bar들의 정박 위치에 대한 2D grid array들
   dx = xs[1]-xs[0];  dy = ys[1]-ys[0] 
   xpos, ypos = \
        np.meshgrid(xs[:-1]+dx/2, ys[:-1]+dy/2, indexing="ij")
   xpos = xpos.ravel();  ypos = ypos.ravel(); zpos = 0
   #막대들의 x,y-축 방향 길이(두께)
   wx = dx;   wy = dy
   wz = zs.ravel()  # 각 bar들의 z-방향 길이(높이: height)
   if ax==None:
     ax = plt.subplot(111, projection='3d')
   ax.bar3d(xpos,ypos,zpos, wx,wy,wz) #, zsort='average')
   plt.show()
   return zs, xs, ys
