#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = "emial.com"
mail_user = "example@email.com"
mail_pass = "mail pass"

sender = "example@email.com"
receivers = ['another@email.com']

message = MIMEText('Python mail test///....','plain','utf-8')
message['From'] = Header("username",'utf-8')
message['To'] = Header ( "test",'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,receivers,message.as_string())
    print ('send successfully..')
except smtplib.SMTPException:
    print ('error : cannot send..')

