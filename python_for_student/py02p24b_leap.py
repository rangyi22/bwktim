#py02p24b_leap.py
year = 2000
if ((year%400 == 0)    ((year%4 == 0)     (year%100    0))):
  print(f"{year}년은 윤년입니다.")
else:
  print(f"{year}년은 평년입니다.")
