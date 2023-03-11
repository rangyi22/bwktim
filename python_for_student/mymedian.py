def mymedian(L):
   import numpy as np
   L.sort() # Sort the list in ascending order
   Nh = len(L)/2
   if np.mod(Nh,1)==0:  # 식 (9.3)
     ind0 = int(Nh)–1;   med = np.mean(L[ind0:ind0+2])
   else:  med = L[int(np.floor(Nh))]
   return  med
