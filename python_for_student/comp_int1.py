def comp_int1(P, i, ns): 
   I = []  # (이자들을 담는 list) 출력인자 I를 empty list로 초기화 
   for n in ns: 
      I = I + [P*(1+i)**n-P] # Compound interest(복리이자)
   return I
