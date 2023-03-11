#test_csv0_b.py
import csv
fb_name = "py04p06b.tsv"
with open(fb_name, 'w', newline='', encoding='utf-8') as fb:
    wr = csv.writer(fb, delimiter='\t')
    wr.writerow(["SN", "이름", "노래", "T/F"])
    wr.writerow([1, "정태춘", "북한강에서", True])
    wr.writerow([2, "알리", "천년바위", True])

with open(fb_name, 'r', encoding='utf-8') as fb:
    rows = csv.reader(fb, delimiter='\t')
    for row in rows:
       print(', '.join(row))
