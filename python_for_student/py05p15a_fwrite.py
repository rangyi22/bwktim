#py05p15a_fwrite.py
fname = "D:/Python/py05p15.txt"
N = 3e7;  i = 0
with open(fname,'w') as f:
   while i<N:
      i += 1
      data = f'{i+1:2d}th line.\n'
      f.write(data)
