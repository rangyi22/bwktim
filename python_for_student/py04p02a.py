#py04p02a.py
fname = 'D:/Python/새파일1.txt'
f = open(fname, "w")
for i in range(0,3):
   data = f'{i+1:2d}th line.'
   if i>0:  data = '\n' + data
   f.write(data)
f.close()
