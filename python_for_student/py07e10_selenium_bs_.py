#py07e10_selenium_bs_.py
SCROLL_PAUSE_TIME = 2
# Get scroll height
last_height=driver.execute_script("return document.body.scrollHeight")
while True:
  # 현재 page의 바닥까지 scroll-down 한다.
  driver.execute_script("window.scrollTo(0, \
                        document.body.scrollHeight);")
  time.sleep(SCROLL_PAUSE_TIME)  # Wait to load page    
  # 새로운 scroll height을 구해서 이전 값과 비교한다.
  new_height = driver.execute_script\
                 ("return document.body.scrollHeight")
  if new_height==last_height: # 더이상 scroll-down할 여지가 없으면
    break  
  last_height = new_height 


from bs4 import BeautifulSoup 
soup = BeautifulSoup(driver.page_source,'html.parser') # 또는 "lxml"
movies = soup.find_all('div', class_="RZEgze")
for movie in movies: 
   div = movie.find('div', class_="b8cIId ReQCgd Q9MA7b")
   a = div.find('a')
   link = a['href']
   title = a.find('div', class_="WsMG1c nnK0zc").get_text()
   span = movie.find('span', class_=" VfPpfd ZdBevf i5DZme)
   price = span.find('span').get_text()
