#py04p04_mail.py
with open("names.txt",'r') as f_names:
with open("mail_body.txt",'r') as f_body:
body = f_body.read() # message 읽음
for names in f_names:
   namelist = names.split(',')
   name_list = list(map(lambda x: x.strip(), namelist))
   for 이름 in name_list:
      mail = "안녕하세요, " + 이름 + "님!\n" + body
      # 각 개인별 파일로 저장
      fname = 이름 + ".txt"
      with open(fname,'w') as f_mail:
          f_mail.write(mail)
