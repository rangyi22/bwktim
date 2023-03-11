#bar3d_my.py
def bar3d_my(X, Y, Z, wx=None, wy=None, ax=None):
   import matplotlib.pyplot as plt
   import numpy as np
   # bar들의 정박 위치에 대한 grid array들
   X = np.array(X); Y = np.array(Y) 
   dx = X[0][1]-X[0][0];  dy = Y[1][0]-Y[0][0]
   # 막대들의 x,y-축 방향 길이(두께)
   if wx==None: wx = dx/2 # bar의 x-축 방향 길이(두께)
   if wy==None: wy = dy/2 # bar의 y-축 방향 길이(폭)
   wx = min([wx, dx]);  wy = min([wy, dy])
   xoffset = wx/2;  yoffset = wy/2
   Xpos, Ypos = X-xoffset, Y-yoffset
   xpos = Xpos.ravel();  ypos = Ypos.ravel(); zpos = 0
   Z = np.array(Z) 
   wz = Z.ravel()  # 각 bar들의 z-방향 길이(높이: height)
   if ax==None:
     ax = plt.subplot(111, projection='3d')
   ax.bar3d(xpos,ypos,0, wx,wy,wz) #, zsort='average')
   plt.show()
