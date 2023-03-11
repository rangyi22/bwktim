#py07p09e_href.py
import re
text = """Link1 <a href="https://www.w3schools.com">
Link2 <a href = "https://www.datacamp.com/">"""
pattern_href = """href\s*=\s*["']([   ]+)["']""" # ^: not
websites = re.       (pattern_href, text)
print(websites)
