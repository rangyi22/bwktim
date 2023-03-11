import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
response = requests.get("https://news.daum.net", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
title = soup.select_one('.link_txt')
print(title.text.strip())