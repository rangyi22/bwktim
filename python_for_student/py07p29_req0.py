#py07p29_req0.py
from bs4 import BeautifulSoup
import requests, time
import json as js
URL0 = "http://www.enuri.com/detail.jsp"
URL_tail="?modelno=44785244&cate=040461&IsDeliverySum=N"
resp = requests.get(URL0+URL_tail)
time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
page_content = resp.content
soup = BeautifulSoup(page_content, 'html.parser')
