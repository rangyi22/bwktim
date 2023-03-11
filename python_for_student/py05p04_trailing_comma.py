#py05p04_trailing_comma.py
def no_trailing_comma(x):
  return x + [4]
def trailing_comma(x):
  return x + [4],
data = [1, 2]
print("Output without , =", no_trailing_comma(data))
print("Output with , =", trailing_comma(data))
