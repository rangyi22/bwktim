#test_csv0_a.py
#https://www.programiz.com/python-programming/writing-csv-files
import csv
fa_name = "py04p06a.csv"
with open(fa_name, 'w', newline='') as fa:
   wr = csv.writer(fa)
   wr.writerow(["SN", "Name", "Contribution"])
   wr.writerow([1, "Linus Torvalds", "Linux Kernel"])
   wr.writerow([2, "Tim Berners-Lee", "World Wide Web"])
   wr.writerow([3, "Guido van Rossum", "Python Language"])

with open(fa_name, newline='') as fa:
    rows = csv.reader(fa, delimiter=',')
    for row in rows:
       print(', '.join(row))
