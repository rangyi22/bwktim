#py02p30b_calendar.py
import calendar
y = 2016;  m = 2 # 몇 년 몇 월
calendar.setfirstweekday(6) #일요일(6)(0: 월요일)을 달력의 맨 왼쪽에
print(calendar.month(y, m, w=3)) # w는 날짜를 표시하는 자리수
