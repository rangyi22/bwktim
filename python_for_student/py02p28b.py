#py02p28b.py
L = [[1,2,3],[5,None,7],[9,10,None,12]]
flag = 0
for e in L:
   for n in e:
      if n==None:
        print('L has None'); flag = 1 
        break
      flag  : 
     break # 위에서 break문이 실행되었으면 바깥 loop도 탈출  
