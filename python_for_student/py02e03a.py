#py02e03a.py 
La = [0, -1, 5, -5, 3, 7]
La1 = []
for x in La1:
   if 0<=x<=5: La1.append(x)
print(La1)
La2 = La.copy()
for x in La:
   if x<0 or x>5: La2.remove(x)
print(La2)
La3 = [x for x in La if 0<=x<=5];  print(La3)
La4 = list(filter(lambda x: 0<=x<=5, La));  print(La4)
La5 = [5 if x>5 else x for x in [-4 if x<-4 else x for x in La]]
print(La5)
