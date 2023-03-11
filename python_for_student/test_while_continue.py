#test_while_continue.py 
import math
while True:
   r = input('\n구의 반경:')
   if r=='': # 사용자가 바로 Enter key를 누른 경우
     break  # while loop를 벗어난다.
   if not r.isnumeric(): # r이 수로 변환이 가능한 문자인가? (표 2.5 참조)
     print('제발 수를, 그것도 0 이상을 주세요!')
     continue  # while loop의 처음(제 3행)으로 돌아간다.
   r = float(r) # 실수형으로 변환
   v = 4/3*math.pi*r**3
   print(f'반경이 {r:.2f}인 구의 부피는 {v:.2f}입니다.')
