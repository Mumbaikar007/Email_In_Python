#imports

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time

class MailOject:

    def __init__(self, to, user, password, subject, message):
        self.to = to
        self.user = user
        self.password = password
        self.subject = subject
        self.message = message

    def Sending_Email(self):
        # smtp gmail


        smtpserver = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)
        #print("Here")
        try:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login ( self.user, self.password)

            #print("Here")

            msg = MIMEMultipart()

            msg['To'] = self.to
            msg['From'] = self.user
            msg['Subject'] = self.subject

            msg.attach(MIMEText(self.message))

            #print("Here")
            #mail
            fp=open('dog.png','rb')
            msg.attach(MIMEImage(fp.read()))
            #print("Here")
            smtpserver.sendmail ( self.user, self.to , msg.as_string())
            #print("Here")
            smtpserver.close()

            print("mailed !!")

        except(smtplib.SMTPException):
            print("There is Somthing Wrong")
