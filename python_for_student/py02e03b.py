#py02e03b.py
Lb = [1, -3, 'four', '7', False, 6]
Lb1 = [x for x in Lb if isinstance(x,(int,float))]
print(Lb1)
Lb2 = [x for x in Lb1 if x != 0 and x%3 == 0] # and -> if  
print(Lb2)
