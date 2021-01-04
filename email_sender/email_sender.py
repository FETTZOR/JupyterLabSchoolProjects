#! /usr/bin/python3

#temp text upd nnew
import smtplib
from email.message import EmailMessage

gmail_user = "hhttajapai@gmail.com"

with open("/home/fetqq/python_course_2021/JupyterLabSchoolProjects/email_sender/pw.txt") as filereader:
    gmail_password = filereader.read()

to = ['hhttajapai@gmail.com']
subject = 'error from application'
body = 'error message'

msg = EmailMessage()
msg.set_content(body)
msg['Subject'] = subject
msg['from'] = gmail_user
msg['To'] = to

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
except:
    print('cannot connect to server')
try:
    server.login(gmail_user, gmail_password)
except:
    print("error with username or pw")
try:
    server.send_message(msg)
except:
    print("error with senging email")
try:
    server.close()
except:
    print("error with server closing")