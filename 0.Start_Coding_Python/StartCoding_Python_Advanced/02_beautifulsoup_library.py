import requests
# Installing bs4 >>> "pip3 install bs4"

from bs4 import BeautifulSoup

# Naver Server에 대화를 시도
response = requests.get("https://www.naver.com")
# Naver에서 html 줌
html = response.text
# html 번역선생님으로 soup 만듬
soup = BeautifulSoup(html, 'html.parser')
# id 값이 NM_set_home_btn인 놈 한개를 찾아냄
word = soup.select_one('#NM_set_home_btn')
# text 요소만 출력
print(word.text)