#bubblesort.py
L = [1,4,3,2,5]
for n in range(len(L)-1,0,-1):
   for i in range(n):
      if L[i] > L[i+1]:
        L[i], L[i+1] = L[i+1], L[i]
print(L)
