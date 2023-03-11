#py07p37_corona.py
import requests, re, csv, json, time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta, tzinfo
URL0 = 'https://www.arcgis.com/apps/opsdashboard/index.html#/'
URL = URL0 + 'bda7594740fd40299423467b48e9ecf6'
res = requests.get(URL).content
#time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
soup = BeautifulSoup(res,'html.parser')
print(soup)
fhtml = open('corona_Korea.html','r')
soup = BeautifulSoup(fhtml,'html.parser')
ggs = soup.find_all('g', # 여기에 들어가는 class명은 수시로 바뀌므로 그에 따라 수동으로 바꿔줘야 한다.
                     class_="amcharts-graph-column amcharts-graph-graphAuto0_1602623061949")
fname = 'corona_Korea.csv'
fcsv = open(fname,'w', newline='') #, encoding='utf8')
wr = csv.writer(fcsv)
for gg in ggs:
   gs = gg.find_all('g')
   N = len(gs)
   for n in range(1,N):
      pattern = '\s?(\d+)월\s?(\d+),\s?(\d+)\s?(\d+)'
      strs = gs[n]['aria-label']
      ds = re.findall(pattern, strs)
      ds = [int(x) for x in ds[0]] # List comprehension
      dt = datetime(ds[2], ds[0], ds[1])
      data = [dt, ds[3]]
      wr.writerow(data)
fhtml.close()
fcsv.close()
