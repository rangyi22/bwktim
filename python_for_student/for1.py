#for1.py (이 code를 저장한 파일이름)
points = [86, 74, 45, 65, 81]
no = 0
for point in points:
   no = no + 1
   if point >= 80:
     result = 'pass'
   else:
     result = 'fail'
   print('The {}th student is {}.'.format(no, result))
