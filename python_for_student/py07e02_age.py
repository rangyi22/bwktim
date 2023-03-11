#py07e02_age.py
from datetime import datetime
def age_in_days(dob):
   # dob = date of birth = (year, month, day) 
   birth_date = datetime(dob[0], dob[1], dob[2])
   time_after_birth = datetime.today() - birth_date
   days_after_birth = time_after_birth.days
   return days_after_birth 
생년월일 = (2000, 4, 8) 
생후몇일 = age_in_days(생년월일)
print(f'태어난 지 {생후몇일}일')
