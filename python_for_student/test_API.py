#test_API.py
import requests 
from bs4 import BeautifulSoup

URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "Your API key" # Openweathermap site에 개인별로 등록해서 받음
params = {'q': 'Seoul', 'appid': API_KEY, 'unit': 'metric'}
res = requests.get(URL, params=params).content
soup = BeautifulSoup(res, 'html.parser')
print(soup)
