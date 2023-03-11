#test_os_listdir.py
import os
Mypath = 'D:/Python/data/'
files = [file for file in os.listdir(Mypath)]
for file in files:
    print(Mypath + file)
