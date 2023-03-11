#py07p34_selenium.py
# > pip install selenium
import requests, re, csv, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

fcsv = open('py07p34.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(fcsv)  # delimiter='\t')
DRIVER_PATH = "D:/ChromeDriver/chromedriver" # My driver path
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
URL = "https://books.google.co.kr/" # 도서(책)만 검색
driver.get(URL)
time.sleep(1) # 창이 열리는 시간을 감안해서 좀 기다려준다.
elem = driver.find_element_by_name("q") # 검색창에다가 query
elem.send_keys("Python")  # Python을 입력하고
elem.send_keys(Keys.RETURN) # Enter key를 누르는 효과를 발생시킨다.
booktitles = [] # 책목록 list를 초기화한다.
page = 1; Npage = 2  # Number of pages to scroll down
SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height=driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, \
                           document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)  # Wait to load page
    bts =  driver.find_elements_by_xpath \
             ('//*[@id="rso"]/div/div/a/h3/span')
    booktitles.extend([bt.text for bt in bts]) # list comprehension
    #Calculate new scroll height, compare it with the last one
    new_height = driver.execute_script\
                   ("return document.body.scrollHeight")    
    if new_height==last_height: #no more to see by scroll-down
      try: driver.find_element_by_link_text("다음").click()  
      except: break  # If there is no more 다음 button
    last_height = new_height
    page += 1
    if page > Npage:  break # 시간을 절약하기 위해 
for booktitle in booktitles:
   csv_writer.writerow([booktitle])
driver.quit() # .close()
fcsv.close()
