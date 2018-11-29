#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'example@email.com'
receivers = ['another@email.com']

message = MIMEText( 'Python test for mail ...','plain','utf-8')
message ['From' ] = Header("Hello,mail",'utf-8')
message['To'] = Header("test",'utf-8')

subject = 'Python SMTP mail test...'
message['Subject'] = Header(subject,'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender,receivers,message.as_string())
    print ( 'send successfully')
except:
    print ("error : cannot send")

