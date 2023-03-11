#py07e03_time.py
from datetime import datetime, timedelta, tzinfo
def sec2day(time_in_sec):
   D_ = divmod(time_in_sec, 86400) # 일(day) 수로
   H_ = divmod(D_[1], 3600) # 3600으로 나눈 몫을 시간(hour) 수로
   m_ = divmod(H_[1], 60) # 60으로 나눈 몫을 분(minute) 수로
   s = m_[1]  # 60으로 나눈 나머지를 초(second) 수로
   return int(D_[0]), int(H_[0]), int(m_[0]), int(s)
날 = 1; 시간 = 1; 분 = 1; 초 = 1
td = timedelta(days=날, hours=시간, minutes=분, seconds=초)
time_in_sec = td.total_seconds() # 86400 + 3600 + 60 + 1
D, H, m, s = sec2day(time_in_sec)
print(f"{time_in_sec}[초] = {D}[날], {H}[시간], {m}[분], and {s}[초]")
