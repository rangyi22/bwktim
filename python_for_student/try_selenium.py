#try_selenium.py
# https://www.youtube.com/watch?v=yQ20jZwDjTE # 나도코딩 유튜브강의 강추
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
DRIVER_PATH = "D:/ChromeDriver/chromedriver" # driver 저장경로
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("https://www.daum.net") # DAUM 나라 입국
time.sleep(2) # 접속을 확실히 하기 위해 기다려준다.
assert "Daum" in driver.title  # 'DAUM'에 제대로 접속됐는지 확인한다.
elem = driver.find_element_by_name("q") # 검색창 click
elem.clear() # 검색창의 default값을 지운다.
elem.send_keys("Selenium") #검색어를 입력한다.
elem.send_keys(Keys.RETURN) # 또는 elem.submit() #검색을 실행시킨다.
time.sleep(2) # 검색결과를 확인하기 위해 기다린다.
driver.get("https://www.youtube.com/?gl=KR") # YouTube 나라 입국
time.sleep(2)
driver.back() # 뒤로 가기 (이전에 방문했던 DAUM site로 돌아간다)
time.sleep(2)
driver.forward() # 앞으로 가기 (YouTube로 다시 돌아온다)
time.sleep(2)
elem = driver.find_element_by_name("search_query") # 검색창 click
elem.clear() # 검색창의 default값을 지운다.
elem.send_keys("Selenium") #검색어를 입력한다.
elem.submit() # 또는 elem.send_keys(Keys.RETURN) #검색을 실행시킨다.
time.sleep(2) # 검색결과를 확인하기 위해 기다린다.
driver.quit() # driver를 종료한다. 
# driver.close() # 이렇게 할 수도 있다.
