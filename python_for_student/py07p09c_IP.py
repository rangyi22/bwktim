#py07p09c_IP.py
import re #<https://www.regular-expressions.info/backref.html>
Ls = ['255.138.13.123', '217.052.04.100', '192.89.31.226', '398.139.180.149']
pattern_IPv4 = "((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"  
for si in Ls: 
   mo = re.     (pattern_IPv4, si)
   if mo: print(          , " is a valid IP address.")
   else: print(si, " is not an IP address.")
