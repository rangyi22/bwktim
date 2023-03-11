#py07p32b_Alexa.py
import requests, re, csv, json
from bs4 import BeautifulSoup
URL = "https://www.alexa.com"
res = requests.get(URL+'/topsites').content
soup = BeautifulSoup(res,'html.parser')
divs = soup.find_all('div', class_="tr site-listing")
for n, div in enumerate(divs):
   rank = div.find('div', class_='td').get_text()
   a = div.find('div', class_='td DescriptionCell').p.a
   link = URL + a['href']
   websitename = a.get_text()
   print(rank, websitename, '\n ', link)
   if int(rank)>4:  break
