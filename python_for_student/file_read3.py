#file_read3.py
f = open("D:/Python/새파일.txt", 'r')
line1 = f.read(10) # 처음부터 10개 영문자 (한글은 그 절반 정도)
print(line1, end='')
line2 = f.read(5) # 10번째부터 14번째 문자까지의 5개 영문자
print(line2, end='')
