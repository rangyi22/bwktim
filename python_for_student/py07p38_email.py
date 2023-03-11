#py07p38_email.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
msg = MIMEMultipart()
msg['From'] = "usernale1@gmail.com"
msg['To'] = "username2@daum.net"
msg['Subject'] = "About Python"
body = "저는 Python을 사랑합니다. 님도 Python을 사랑하면 좋겠습니다."
msg.attach(MIMEText(body, 'html'))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(msg['From'], "password1")
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
