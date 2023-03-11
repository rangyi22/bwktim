#py05p15c_generator.py
def csv_reader(fname):
   for row in open(fname, 'r'):
      yield row
