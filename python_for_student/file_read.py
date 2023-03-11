#file_read.py
f = open("D:/Python/새파일.txt", 'r') # 'r'(읽기 mode 설정)은 생략가능
while True:
   line = f.readline()   
   if not line: break
   print(line, end='')
f.close()
