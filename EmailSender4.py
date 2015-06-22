#!/usr/bin/env python3

import smtplib

session = smtplib.SMTP('smtp.gmail.com', 587)
session.ehlo()
session.starttls()
session.login('4evarelentless@gmail.com','password')
headers = "\r\n".join(["from: " + '4evarelentless@gmail.com',
                       "subject: " + "test",
                       "to: " + 'okeonwuka@gmail.com',
                       "mime-version: 1.0",
                       "content-type: text/html"])

# body_of_email can be plaintext or html!                    
content = headers + "\r\n\r\n" + "body_of_email"
session.sendmail('4evarelentless@gmail.com', 'okeonwuka@gmail.com', content)