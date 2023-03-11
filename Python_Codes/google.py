from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

baseUrl = 'https://www.google.com/search?q='
plusUrl = input('What do you want to search for? : ')
url = baseUrl + quote_plus(plusUrl)

print(url)

# driver = webdriver.Chrome()
# driver.get(url)