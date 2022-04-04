from smtplib import SMTP

# subject = "Konu"
# message = "webmail.abdullahaligun.com -465"
# content = "Subject: {0} \n {1}".format(subject,message)
#
# myMailAdress = "mail@pys.abdullahaligun.com"
# password = "xa1@6C4x"
# # Kime Gönderilecek Bilgisi
# sendTo = "hacklojen01@gmail.com"
#
# mail = SMTP("webmail.abdullahaligun.com",465)
# mail.ehlo()
# mail.starttls()
# mail.login(myMailAdress, password)
# mail.sendmail(sendTo, sendTo, content.encode("utf-8"))


# import smtplib
#
# content = "merhaba"
# mail = smtplib.SMTP("smtp.gmail.com",587)
# mail.ehlo()
# mail.starttls()
# mail.login("info.kouai@gmail.com","")
# mail.sendmail("info.kouai@gmail.com","hacklojen01@gmail.com",content)

import datetime

print(datetime.datetime.now())
