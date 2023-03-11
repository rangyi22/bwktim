import requests
from bs4 import BeautifulSoup

header = {'User-agent' : 'Mozila/2.0'}
response = requests.get("https://news.daum.net", headers=header)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select('.link_txt')
#print(titles)
for title in titles:
    print(title.text.strip())