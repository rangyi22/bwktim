#test_csv1.py
import csv
Mypath='D:/Python/data/'
fcsv = Mypath+'grade.csv'; fcsv2 = Mypath+'grade2.csv'
fr = open(fcsv, newline='')
reader = csv.DictReader(fr, skipinitialspace=True)
with open(fcsv2, 'w', newline='') as fw:
   i = 0  #  다음 for loop index i를 초기화
   for row in reader:       
      print('row =', row)
      if i==0:
        keys = list(row.keys())
        keys.append('Sum')
        writer = csv.DictWriter(fw, fieldnames=keys)
        writer.writeheader()
      scores = list(row.values())[1:4] 
      row['Sum'] = sum(map(float, scores))
      writer.writerow(row) # row는 list 또는 dictionary이어야 한다.
      i += 1
fr.close()
