#py07e07_bs.py
import requests, re, csv, time
from bs4 import BeautifulSoup
URL_Naver_comic ="https://comic.naver.com"
res = requests.get(URL_Naver_comic)
time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
soup = BeautifulSoup(res.text,'html.parser') # 또는 "lxml"
fcsv = open('py07e07.csv', 'w', encoding='utf-8-sig', newline='')
csv_writer = csv.writer(fcsv) # delimiter='\t') #요소별로 다른 열에 저장
csv_writer.writerow(['title', 'URL'])
aa = soup.find_all('a', href=re.compile('toon'), 
         onclick=True, title=True) # onclick, title 속성이 있는 걸로
for a in aa:
   title = a.get_text().strip()
   link = URL_Naver_comic + a['href']
   print(title, '\n ', link)
   csv_writer.writerow([title, link])
fcsv.close()
