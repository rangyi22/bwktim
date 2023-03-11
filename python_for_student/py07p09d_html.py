#py07p09d_html.py
import re
s = """<h1>Big and Important Header</h1>
<h2>Slightly Less Big Header</h2> <h3>Sub-Header</h3>"""
pattern_html = "<     >"
html_tags = re.       (pattern_html, s)
# 주어진 pattern을 가진 문자열을 삭제하기
pat_tag = re.       (pattern_html)
text = re.   (pat_tag, '', s)
print("text =", text)
