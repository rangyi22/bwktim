#py02p30a_calendar.py
y = 2016;  m = 2 # 몇 년 몇 월
# y년이 윤년인가 아닌가?
윤년 = False  # default로 윤년이 아닌 평년이라고 가정한다.
if y%400 == 0 or (y%4 == 0 and y%100 != 0):
  윤년 = True
# m월의 날수 구하기
if m == 2:
  if 윤년:  nday = 29
  else:  nday = 28
elif  m in {1, 3, 5, 7, 8, 10, 12}:  nday = 31
else:  nday = 30
# m월 1일의 요일 구하기 (0: 일, 1: 월, 2: 화,....)
# Zeller 공식 (P2.30.1,2) 
d = 1  # 어느 달이든 1일
if m <= 2:  y1 = y - 1;  m1 = m + 12
w = (y1 + y1//4 - y1//100 + y1//400 + (13*m1+8))//5 + d) % 7
# 달력을 print하기 
print(f"         {y}년 {m}월")
weekdays = ['일','월','화', '수', '목', '금', '토']
for wd in weekdays:
   print(f"{wd:>3s}", end='')
print()
print(' '*4*w, end='') # 1일이 몇 요일인가에 따라 들여쓰기
for day in range(nday):
   if w % 7 == 0:  print() # 7일, 즉 1주일마다 줄 바꾸기
   print(f'{day+1:4d}', end='')
   w += 1
