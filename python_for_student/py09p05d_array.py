#py09p05d_array.py
import numpy as np

A = np.array([[1, 3, 2],[8, 7, 4],[5, 9, 6]])
indices = np.zeros((1,2))  # 색인행렬의 초기화
#indices = np.empty((1,2), dtype=int) # Alternatively
M,N = A.shape # 행 개수(row size)와 열 개수(column size)
for m in range(M):
   for n in range(N): 
      if A[m][n] > ?:
        indices = np.append(indices, np.array([[?,?]]), axis=0)
indices = np.delete(indices, 0, axis=0)
print('indices =\n', indices)
