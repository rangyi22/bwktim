#py05p15b_fread.py
def csv_reader(fname):
   f = open(fname)
   result = f.read().split('\n')
   return result
fname = "D:/Python/py05p15.txt"
csv_gen = csv_reader(fname)
row_count = 0
for row in csv_gen:
   row_count += 1
   if row_count % 1e7 == 0:
     print(row, end='')
