#test_csv.py
import csv
Mypath='D:/Python/data/'
Fcsv = Mypath+'grade.csv'; fcsv1 = Mypath+'grade1.csv'
fw = open(fcsv1, 'wt', newline='') # encoding='utf8'
writer = csv.writer(fw)
with open(fcsv, newline='') as fr:
    reader = csv.reader(fr, delimiter=',', skipinitialspace=True)
    i = 0  #  다음 for loop index i를 초기화
    for row in reader:
       print('row =', row)
       if i==0:  s = 'Sum'
       else:   s = sum(map(float, row[1:4]))
       row.append(s)
       writer.writerow(row) # row는 list 또는 dictionary이어야 한다.
       i += 1
fw.close()
