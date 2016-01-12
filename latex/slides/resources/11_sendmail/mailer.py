#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText


def buildmessage():
    message = MIMEText('Text der E-Mail.')

    # set the sender of your mail
    message['From'] = 'Sender name <sender@example.com>'
    # set the receiver of your mail
    message['To'] = 'Receiver name <receiver@example.com>'

    message['Subject'] = 'Betreff der E-Mail'

    return message


def main():
    message = buildmessage()
    server = 'Servername'
    port = 587  # This is the default Port of an smtp server

    try:
        with smtplib.SMTP(host=server, port=port) as smtpObj:
            smtpObj.starttls()
            smtpObj.login('user', 'pass')
            smtpObj.send_message(message)
    except SMTPException:
        print("Error: unable to send email.")

if __name__ == '__main__':
    main()
