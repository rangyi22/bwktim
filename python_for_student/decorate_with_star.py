def decorate_with_star(func):
   def inner(*args, **kwargs): 
      print("*"*10 + func.__name__ + ' begins' + "*"*10)
      func(*args, **kwargs)
      print("*"*10 + func.__name__ + ' ends' + "*"*10)
   return inner
