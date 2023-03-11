#generator_fibonacci.py
def gen_fibo():
   x, y = 0, 1
   while True:
      x, y = y, x+y
      yield x
g_fb = gen_fibo()
fbs = [next(g_fb) for _ in range(5)]
print(f"fibonacci nos using gen_fibo() =\n{fbs}")
