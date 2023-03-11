#open_html_beautifulsoup.py
def html_beautifulsoup(filename):
   from bs4 import BeautifulSoup 
   with open(filename) as fp:
       soup = BeautifulSoup(fp, "html.parser")
   return soup
