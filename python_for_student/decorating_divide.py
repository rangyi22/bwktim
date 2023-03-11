#decorating_divide.py
# <https://www.programiz.com/python-programming/decorator>
def divide(a, b):
    print(a/b)
def decorate_divide(func):
   def div(a, b):
      print("I am going to divide", a, "by", b)
      if b==0:
        print("Whoops! Zero-division is impossible.")
        return
      return func(a, b)
   return div
