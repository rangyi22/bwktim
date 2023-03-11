#py07p24_csv.py
import csv
def generator1(fname):
   with open(fname, 'rt') as f:
      reader = csv.reader(f, skipinitialspace=True,
                          delimiter=',', quotechar="'")
      for line in reader:   yield line
gen = generator1("addresses.csv")
with open('addresses2.csv', 'wt', newline='') as f:
   writer = csv.writer(f)
   while True:
      try:   writer.writerow(next(gen))
      except: break  # 실행오류가 발생하면 while loop 탈출
