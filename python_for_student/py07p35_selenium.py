#py07p35_selenium.py
from selenium import webdriver
DRIVER_PATH = "D:/ChromeDriver/chromedriver" # driver path
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.geeksforgeeks.org/")
divs = driver.find_elements_by_css_selector('div.content')
n = 0
for div in divs:
   es = div.find_elements_by_css_selector('div.head')
   #es = div.find_elements_by_class_name("head")# 또는 이렇게
   for e in es:
      try:
         a = e.find_element_by_css_selector('a')
      except:
         continue
      n += 1
      title = a.text
      link = a.get_attribute('href')
      print(f'{n:2d}: {title}\n    link = {link}')
