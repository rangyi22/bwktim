#py04p08_URL.py
URL = "https://docs.python.org/2/library/urllib.html"
print("Using urllib.request.urlopen():")
import urllib.request
resp1 = urllib.request.urlopen(URL)
resp1_bytes = resp1.read() # bytes형 data
print(resp1_bytes[0:61]) # 처음 61개 byte만 보자.
print("\n\nUsing requests.get():")
import requests
resp2 = requests.get(URL) # bytes형 data
resp2_bytes = resp2.content
print(resp2_bytes[0:61])
#resp2_str = resp2_bytes.decode('utf-8')
#print(resp2_str[0:61])
#resp2_bytes1 = resp2_str.encode('utf-8')
#print(resp2_bytes1[0:61])
