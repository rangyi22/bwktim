#generator_inf.py
def gen_even():  # generator function
   n = 0
   while True:
      yield n
      n += 2
