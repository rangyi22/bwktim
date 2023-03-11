def comp_int5(P, i=0.05, n=10):
   I = P*(1+i)**n-P  # Compound interest(복리이자)
   print(f'Interest = {I:6.1f}') 
