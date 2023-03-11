#py07e09_selenium.py
# https://www.youtube.com/watch?v=1b7pXC1-IbE # 조코딩 유튜브강의 참조
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, csv, time
fcsv = open('py07e09.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(fcsv) #, delimiter='\t')
DRIVER_PATH = "D:/ChromeDriver/chromedriver" # driver 저장경로
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("Selenium") # 검색어를 입력한다
elem.submit() # 또는 elem.send_keys(Keys.RETURN) #검색을 실행시킨다.
다음 = 1; # 찾아볼 page 번호
while True:
   divs = driver.find_elements_by_css_selector("div.yuRUbf")
   for div in divs:
      a = div.find_element_by_tag_name("a")
      link = a.get_attribute('href')
      title = a.find_element_by_css_selector("h3>span").text
      print(title, link)
      csv_writer.writerow([title, link]) 
   try: 
      if 다음 >= 2:  break # 시간을 절약하기 위해 
      driver.find_element_by_link_text("다음").click() 
      다음 += 1
      continue
   except: break  # 더이상 "다음" button이 없으면
driver.quit() # .close()
fcsv.close()
