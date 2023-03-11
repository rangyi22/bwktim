#py07p09b_URL.py
import re
s = """ab .. https://code.tutsplus.com/tutorials/8-regular-expressions-you-should-know--net-6149/ .xyz <A HREF ="http://msdn2.microsoft.com/"> MSDN Home Page</A></P>"""
pattern_URL = '(https ://[          ]+)'
L = re.        (pattern_URL, s)
print("URLs =", L)
