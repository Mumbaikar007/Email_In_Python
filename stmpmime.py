
import smtplib
from os.path import basename
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import time

class MailOject:

    def __init__(self, to, user, password, subject, message, attachment_list):
        self.to = to
        self.user = user
        self.password = password
        self.subject = subject
        self.message = message
        self.attachment_list =attachment_list

    def Sending_Email(self):



        smtpserver = smtplib.SMTP('smtp.gmail.com', 587, timeout=30)

        try:
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login ( self.user, self.password)

            msg = MIMEMultipart()

            msg['To'] = self.to
            msg['From'] = self.user
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = self.subject

            msg.attach(MIMEText(self.message))


            # mail attachments

            for file in self.attachment_list:
                print(file, basename(file))
                rfile = open( file, 'rb')
                part = MIMEApplication(
                    rfile.read(),\
                    Name=basename(file)
                    )
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file)
                msg.attach(part)

            #fp = open('messi5.jpeg', 'rb')
            #msg.attach(MIMEImage(fp.read()))



            smtpserver.sendmail ( self.user, self.to , msg.as_string())

            smtpserver.close()

            print("mailed !!")

        except(smtplib.SMTPException):
            print("There is Somthing Wrong")
