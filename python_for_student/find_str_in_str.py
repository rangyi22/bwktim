#find_str_in_str.py
s = 'Is a pineapple a kind of apple?'
w = 'apple';  lw = len(w)
N = s.count(w)
for n in range(0,N):
   if n==0:  s1 = s
   m = s1.    (w)
   print(f"The {n+1}th 'apple' is located at [{m}:{m+lw-1}].")
   s1 = s1[0:m] + '-'*   + s1[m+  :]
