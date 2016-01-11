#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText


def buildmessage():
    message = MIMEText('Text der E-Mail.')

    # set the sender of your mail
    message['From'] = '{nam} <{mail}>'.format(nam='Name des Absenders',
                                              mail='Mail des Absenders')
    # set the receiver of your mail
    message['To'] = '{nam} <{mail}>'.format(nam='Name des Empfaengers',
                                            mail='Mail des Empfaengers')
    # you might wanna set a BCC?
    # message['Bcc'] = 'root <bcc-receiver@mail.com>'
    message['Subject'] = 'Betreff der E-Mail'

    return message


def main():
    message = buildmessage()
    server = 'Servername' + ':' + 'Port'

    try:
        smtpObj = smtplib.SMTP(server)
        smtpObj.starttls()
        smtpObj.login('user', 'pass')
        smtpObj.send_message(message)
        smtpObj.quit()
    except SMTPException:
        print("Error: unable to send email.")

if __name__ == '__main__':
    main()
