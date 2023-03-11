#py02e02a.py
L = [3, 3, 2, 1, 2, 5]
Lu = [] # 빈 (empty 또는 null) list 
for x in L:
   if x not in Lu: 
     Lu.append(x) 
print(Lu)
