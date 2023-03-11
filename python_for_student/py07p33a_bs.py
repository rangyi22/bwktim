#py07p33a_bs.py
import requests, re, csv, time
from bs4 import BeautifulSoup
fcsv = open('py07p32a.csv', 'w', encoding='utf8', newline='')
csv_writer = csv.writer(fcsv)
csv_writer.writerow(['Quote', 'Author'])
Npages = 3
for page in range(1,Npages):
   URL = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
   resp = requests.get(URL)
   time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
   soup = BeautifulSoup(resp.content, 'html.parser')
   scripts = soup.find("script", {'src': '/static/jquery.js'})
   qas = scripts.next_sibling.next_sibling.children
   for qa in qas:
      qa_string = qa.string
      quotes = re.findall(r'\\(u.+)\\u', qa_string)
      authors = re.findall('"name": "(.+)"', qa_string)
      for quote, author in zip(quotes, authors):
         print(quote[6:-2], author)
         csv_writer.writerow([quote[6:-2], author])
fcsv.close()
