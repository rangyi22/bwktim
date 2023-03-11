#py02p24a_leap.py
year = 2000
if (year % 4) == 0:
  if (year % 100) == 0:
    if (year % 400) == 0:
      print(f"{year}년은 윤년입니다.")
    else:
      print(f"{year}년은 평년입니다.")
  else:  print(f"{year}년은 윤년입니다.")
else:
  print(f"{year}년은 평년입니다.")
