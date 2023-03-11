#while1.py
points = [86, 74, 65, 81]
no = 0
while points: 
  point = points[0]
  no = no + 1
  if point >= 80:
    result = 'pass'
  else:
    result = 'fail'
  print(f'{no:2d} 번째 학생: {result}.')
  del points[0] # 매 iteration마다 첫 번째 요소를 지워서 텅 빌 때까지 반복
