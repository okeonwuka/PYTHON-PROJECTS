#! /usr/bin/env python
import smtplib

content = 'Welcome to spotfire'

mail = smtplib.SMTP('smtp.gmail.com',465)

mail.ehlo()

mail.starttls()

mail.login('okeonwuka@gmail.com','4Evarelentle$$')

mail.sendmail('okeonwuka@gmail.com','okeonwuka@yahoo.com', content)

mail.close()


# Just ignore this line

