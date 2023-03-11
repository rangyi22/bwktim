#py07p36_emails.py
import requests, re, csv, json
from bs4 import BeautifulSoup
URL0 = "https://www.eecs.psu.edu/departments/"
URL='https://www.eecs.psu.edu/departments/ee-faculty-list.aspx'
res = requests.get(URL).content
time.sleep(2) # data 내려받는 시간을 고려해서 좀 기다려준다.
soup = BeautifulSoup(res,'html.parser')
print(soup) 
fcsv = open('py07p36.csv', 'w', encoding='utf8', newline='')
csv_writer = csv.writer(fcsv)
csv_writer.writerow(['Name', 'Email address', 'Web sites'])
divs = soup.find_all('div',
                     class="fluid results-individual-revised")
for div in divs:
   pattern_email = '[\w\.\-]+ [\w\.\-]+'
   email = div.find('a', text=re.compile(pattern_email))
   #email = div.find('a', text=re.compile('@'))
   if email is None: email_addr = 'None'
   else:  email_addr = email.text
   directory = div.find('p', {'class':       })
   if directory is None:  (name, link) = ('None', 'None')    
   else:
     dir = directory.find('a')
     name = dir.text
     link = URL0 + dir['h   '] # absolute + relative URL
     if link is None: link = 'None'
   csv_writer.writerow([name, email_addr, link])
fcsv.close()
