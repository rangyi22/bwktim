def comp_int4(P, i, n):
   Is = P*i*n  # Simple interest(단리이자)
   Ic = P*(1+i)**n-P  # Compound interest(복리이자)   
   return Is, Ic
