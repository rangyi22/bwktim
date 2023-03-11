#py07e08_bs.py
import requests, re, csv, time
from bs4 import BeautifulSoup
URL_쿠팡 = 'https://www.coupang.com/np/search?q=%EB%... =auto"
My_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; ...."
headers = {'User-Agent': My_user_agent} 
resp = requests.get(URL_쿠팡, headers=headers) 
soup = BeautifulSoup(resp.text,'html.parser') # 또는 "lxml"
lis = soup.find_all('li', class_=re.compile("search-p\.*"))
for li in lis:
   상품명 = li.find('div', attrs={'class':'name'}).get_text()
   가격 = li.find('strong', class_='price-value').get_text()
   rate_cnt = li.find('span', class_='rating-total-count')   
   if rate_cnt:  # 품평이 있는 것들만
     품평수 = int(rate_cnt.get_text().strip('()'))
     print(상품명, 가격, 품평수)
