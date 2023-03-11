def comp_int3(**kwargs):
   if len(kwargs)<1:  return
   P= kwargs['P'];   i = kwargs['i'];   n = kwargs['n']
   I = P*(1+i)**n-P  # Compound interest(복리이자)
   print(f'Interest with {kwargs} = {I:6.1f}')   
   return I
