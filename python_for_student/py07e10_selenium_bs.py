#py07e10_selenium_bs.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re, csv, time
fcsv = open('py07e10.csv', 'w', newline='', encoding='utf-8-sig')
csv_writer = csv.writer(fcsv) # delimiter='\t')
DRIVER_PATH = "D:/ChromeDriver/chromedriver" # driver 저장경로
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://play.google.com/store/movies/top")
csv_writer.writerow(['제목(title)', '가격(price)', 'link'])
movies = driver.find_elements_by_css_selector("div.RZEgze")
for movie in movies:
   a = movie.find_element_by_css_selector \
                    ("div.b8cIId.ReQCgd.Q9MA7b>a")
   link = a.get_attribute('href')
   title = a.find_element_by_css_selector("div.WsMG1c.nnK0zc").text
   price = movie.find_element_by_css_selector \
               ("span.VfPpfd.ZdBevf.i5DZme>span").text
   csv_writer.writerow([title, price, link])
driver.quit() # .close()
fcsv.close()
