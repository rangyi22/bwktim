#file_read2.py
f = open("D:/Python/새파일.txt", 'r')
for line in f:
   print(line, end='')
f.close()
