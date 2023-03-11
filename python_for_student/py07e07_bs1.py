#py07e07_bs1.py
import requests, re, csv, time
from bs4 import BeautifulSoup
URL_Naver_comic ="https://comic.naver.com"
.. . . . . . . . . . . . .
lis = soup.find_all('li', class_=re.compile('rank'))
for li in lis:
   rank = li['class'][0][4:]
   a = li.a   
   title = a['title']
   link = URL_Naver_comic + a['href']
   print(rank, title, '\n ', link)
   csv_writer.writerow([rank, title, link])
fcsv.close()
