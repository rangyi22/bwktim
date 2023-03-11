#py02p28a.py
L = [[1,2,3],[5,None,7],[9,10,None,12]]
for e in L:
   for n in e:
      if n==None:
        print('L has None') 
        break
   else: # 위 for loop에서 break문이 실행되지 않은 경우에만
      continue  
   break # 위 for loop에서 break문이 실행되었으면 바깥 loop 탈출  
