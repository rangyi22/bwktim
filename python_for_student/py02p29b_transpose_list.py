#py02p29b_transpose_list.py
A = [[1, 2, 3, 4], [4, 5, 6, 8]]
AT = []
for i in range(len(A[0])):
   rowT = []
   for row in A:
      rowT.append(row[i])
   AT.append(rowT)
print(AT)
