#test_csv2.py
import csv
Mypath='D:/Python/data/'
fcsv = Mypath+'addrs.csv'; fcsv1 = Mypath+'addrs1.csv'
fr = open(fcsv, newline='')
reader = csv.reader(fr, skipinitialspace=True, quotechar="'")
fw = open(fcsv1, 'w', newline='')
writer = csv.writer(fw)
for row in reader:
   print('row =', row)
   writer.writerow(row) # row는 list 또는 dictionary이어야 한다.
fr.close(); fw.close()
