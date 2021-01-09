from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
# set up the SMTP server
from random import random, randint
from email.message import EmailMessage


def sendemail(email, code):
    EMAIL_ADDRESS = 'chimi7827@gmail.com'
    EMAIL_PASSWORD = 'chimichangaslovessiege'

    # Create empty Email Message object
    msg = EmailMessage()

    msg['Subject'] = '2fa code:' + str(code)
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = email
    msg.set_content('this is a 2 factor code')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

      smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
      smtp.send_message(msg, from_addr=EMAIL_ADDRESS, to_addrs=email)




