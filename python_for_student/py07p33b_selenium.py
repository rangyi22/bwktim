#py07p33b_selenium.py
# > pip install selenium
from selenium import webdriver
import csv, time
DRIVER_PATH="D:/ChromeDriver/chromedriver"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
fcsv = open('py07p33b.csv', 'w', encoding='utf8', newline='')
csv_writer = csv.writer(fcsv)
csv_writer.writerow(['Quote', 'Author'])
Npages = 3
for page in range(1,Npages):
   URL = "http://quotes.toscrape.com/js/page/" + str(page) + "/"
   driver.get(URL)
   time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
   quotes = driver.find_elements_by_class_name("quote")
   for quote in quotes:
      quote_text = quote.find_element_by_class_name('text').text
      author = quote.find_element_by_class_name('author').text
      csv_writer.writerow([quote_text, author])                
driver.quit() # .close()
fcsv.close()
