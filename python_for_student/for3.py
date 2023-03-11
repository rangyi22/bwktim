#for3.py
for m in range(2,5):      # ①번 for문
   for n in range(1,10):   # ②번 for문
      mn=m*n
      print("%4d" % mn, end=" ") # 같은 줄에서 1문자 간격으로 
   print('')  # to the next line
