#nested_func.py
def comp_int6(P, i, n=1, 단복='단복'):
   Ic = 0;  Is = 0  # default 값들
   def int_s(P, i, n):
      global Is
      Is = P*i*n  # Simple interest(단리이자)      
      return Is
   def int_c(P, i, n):
      nonlocal Ic
      Ic = P*(1+i)**n-P  # Compound interest(복리이자)   
      return Ic
   Int_s = int_s(P, i, n)
   Int_c = int_c(P, i, n)
   print(f"Is (int_s()함수 안 global) = {Is}")
   print(f"Ic (int_c()함수 안 nonlocal)= {Ic}")   
   if 단복 == '단': Int = Int_s 
   elif 단복 == '복': Int = Int_c 
   else: Int = (Int_s, Int_c)     
   return  Int
