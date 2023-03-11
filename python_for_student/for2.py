#for2.py
points = [86, 74, 95, 65, -35, 81] # len(points) = 5
n = 0
for point in points:
   n = n + 1
   if point < 0:
     print('Something wrong in the data!')
     break
   elif point < 80:
     print(f'The {n}th student with point={point} has failed.')
     continue
   else:
     pass
   print(f'The {n}th student with point={point} has passed.')

