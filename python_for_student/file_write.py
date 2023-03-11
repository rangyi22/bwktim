#file_write.py
f = open("D:/Python/새파일.txt", 'w')
for i in range(0,3):   
   data=f'{i+1:2d}th line.\n'
   f.write(data)
f.close()
