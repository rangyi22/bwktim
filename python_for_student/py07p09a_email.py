#py07p09a_email.py
import re
email_list =  """python12@@google.com, matlab.3@hotmail.com,  
   exel-56@hotmail.com"""
pattern_email = '[\w\.\-]+@[       ]+' # (?:\.com|net|edu)'
emails = re.       (pattern_email, email_list)
print(emails)
