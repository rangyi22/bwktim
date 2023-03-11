#py02p38.py 
L = [1, 2, [3, 4, [5, 6, 7]]];  L1 = []
list_nested = 1 # L이 일단 nested list인 것으로 가정한다.
n = 0  # while loop index
while list_nested > 0: # L이 (잠재적으로) nested이면 ..
   L1 = [];  n += 1
   for item in L:
      list_nested = 0 
      if type(item) ==     : # item이 list인가?
        L1.      (item)  # L1에다 list item의 각 요소들을 첨가해.
        list_nested = 1 # L이 item list를 포함하고 있네
      else: 
        L1.      (item) # 하나의 요소 item을 첨가해.
   L = L1.copy()
print(n, L1)
