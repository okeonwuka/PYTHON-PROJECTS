#! /usr/bin/env python

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 465)

#Next, log in to the server
server.login("okeonwuka@gmail.com", "password")

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("okeonwuka@gmail.com", "okeonwuka@gmail.com", msg)
server.quit()