#py07p31_영어.py
from bs4 import BeautifulSoup
import requests, csv, time
URL0 = "https://basicenglishspeaking.com/"
URL = URL0 + "daily-english-conversation-topics/"
fcsv = open('py07p31.csv', 'w', encoding='utf8', newline='')
csv_writer = csv.writer(fcsv)
csv_writer.writerow(['Subjects','Question','Answer','URL'])
resp = requests.get(URL)
soup = BeautifulSoup(resp.content, 'html.parser')
print(soup.prettify())
divs = soup.find_all('div', {'class': "tve-froala"})
n = 0;  N = len(divs)   
for div in divs:
   links = div.find_all('a')
   for link in links:
      n += 1
      if n>2:  break
      subject = link.text ;  URLn = link['href']
      print(f"\n{n}/{N}: {subject}")  
      respn = requests.get(URLn)
      time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
      soupn = BeautifulSoup(respn.content, 'html.parser')
      print(soupn.prettify())
      qas=soupn.find_all('div', {'class':"sc_player_container1"})
      n1 = 0
      for qa in qas:
         n1 += 1;  m = int((n1+1)/2)
         if n1>4: break
         print(f"qas[{n1}]:\n", qa)
         if n1 % 2 == 1: # qa가 홀수 번째라면
           Q = qa.next_sibling  # 그 뒤(다음) 형제가 질문
           print(f"Q[{m}]:{Q}")
         else:   qa가 짝수 번째라면
           A = qa.next_sibling  # 그 뒤(다음) 형제가 대답
           print(f"A[{m}]:{A}")       
           csv_writer.writerow([subject, Q, A, URLn])        
fcsv.close()
