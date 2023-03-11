#test_csv0_c.py
import csv
fc_name = "py04p06c.csv"
with open(fc_name, 'w', newline='', encoding='utf-8-sig') as fc:
    wr = csv.writer(fc, delimiter=',')
    wr.writerow("정태춘")
    wr.writerow("알리")

with open(fc_name, 'r', encoding='utf-8-sig') as fc:
    rows = csv.reader(fc, delimiter=',')
    for row in rows:
       print(', '.join(row))
