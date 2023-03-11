#py09p05a_array.py
import numpy as np

A = np.array([[1, 3, 2],[8, 7, 4],[5, 9, 6]])
where = np.where(A > ?)
print('Entries > 7:')
for indices in zip(where[?], where[1]):
   m, n = indices[0], indices[?] 
   print(f'A({m},{?}) = {A[?][n]}')
