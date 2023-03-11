#py07p32a_marketcap.py
import requests, re, csv, json
from bs4 import BeautifulSoup
URL = "https://companiesmarketcap.com/"
res = requests.get(URL).content
soup = BeautifulSoup(res,'html.parser')
trs = soup.find_all('tr')
for n, tr in enumerate(trs):
   td = tr.find('td', class_='td-right')
   if td:  rank = td.get_text()
   else:  continue
   td1 = tr.find('td', class_='name-td')
   a = td1.find('div', class_='name-div').find('a')
   link = URL + a['href']
   websitename = a.div.get_text()
   print(rank, websitename, '\n ', link)
   if int(rank)>4:  break
