#! /usr/bin/python3

#temp text upd nnew
import smtplib
from email.message import EmailMessage
def main():
    gmail_user = "hhttajapai@gmail.com"

    with open("/home/fetqq/python_course_2021/JupyterLabSchoolProjects/email_sender/pw.txt") as filereader:
        gmail_password = filereader.read()

    to = ['hhttajapai@gmail.com']
    subject = 'very important message'
    body = 'https://youtu.be/dQw4w9WgXcQ'

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['from'] = gmail_user
    msg['To'] = to

    while True:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
        except:
            print('cannot connect to server')
            break
        try:
            server.login(gmail_user, gmail_password)
        except:
            print("error with username or pw")
            break
        try:
            server.send_message(msg)
        except:
            print("error with senging email")
            break
        try:
            server.close()
        except:
            print("error with server closing")
            break
        break

if __name__ == "__main__":
    main()