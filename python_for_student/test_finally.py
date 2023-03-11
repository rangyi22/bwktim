#test_finally.py
f = open("test.txt", "w")
try:
    f.write("We try writing a file ... ")
    f.write(42) # 숫자는 파일에 쓰여질 수가 없으므로 TypeError가 발생한다. 
except:
    print("예외가 발생했습니다.") 
finally: 
    f.close() # 위에서 발생한 Error의 효과가 파급되기 전에 수행된다.
    print("파일이 닫혀졌나요?", f.closed)
