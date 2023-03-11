def comp_int2(P, i, *args): 
   I = [] # (이자들을 담는 list) 출력인자 I를 empty list로 초기화
   for n in args: 
      I.append(P*(1+i)**n-P) # Compound interest(복리이자)
   return I
