import smtplib

FROMADDR = "cmpnb.sfit2015@gmail.com"
LOGIN    = FROMADDR
PASSWORD = "Cmpnb_123"
TOADDRS  = ["tanmay.sankhe97@gmail.com"]
SUBJECT  = "Test"

msg = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR, ", ".join(TOADDRS), SUBJECT) )
msg += "some text\r\n"

server = smtplib.SMTP('smtp.gmail.com', 587)
try:
	server.set_debuglevel(1)
	server.ehlo()
	server.starttls()
	server.login(LOGIN, PASSWORD)
	#server.sendmail(FROMADDR, TOADDRS, msg)
	server.quit()
except(smtplib.SMTPException):
	print("There is Somthing Wrong")