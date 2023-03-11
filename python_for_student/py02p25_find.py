#py02p25_find.py
L = [1, 7, 3, 6, 2, 8, 4, 9, 5]
Item = 2  # item to find
pos = [] 
for n in range(0,len(L)):
   if L[n] == Item:  pos.append(n)
   else:             continue
if len(pos) > 0: print(f"{str(Item)} at {pos} of L.")
else:  print(f"{str(Item)} has not been found in L.")
