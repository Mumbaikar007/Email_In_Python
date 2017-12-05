#imports

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time


# smtp gmail
to = ""
user = ""
password = ""

smtpserver = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
#print("Here")
try:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login ( user, password)

    #print("Here")

    msg = MIMEMultipart()

    msg['To']=to
    msg['From']=user
    msg['Subject']='Dog'

    msg.attach(MIMEText("Hello"))

    #print("Here")
    #mail 
    fp=open('dog.png','rb')
    msg.attach(MIMEImage(fp.read()))
    #print("Here")
    smtpserver.sendmail ( user, to , msg.as_string())
    #print("Here")
    smtpserver.close()

    print("mailed !!")

except(smtplib.SMTPException):
	print("There is Somthing Wrong")
