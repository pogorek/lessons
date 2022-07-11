# 18 SENDING EMAIL AND TEXT MESSAGES

#! ezgmail - doesn't work - oudated?
# import ezgmail
# import os
# # os.chdir(r'D:\PROGRAMOWANIE\GIT\school\sweigart_automate\credentials.json')
# os.chdir(r'/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate')
# ezgmail.init()

import os

import smtplib
EMAIL_USER = os.environ.get('EMAIL_USER_BOT')
EMAIL_PASS = os.environ.get('EMAIL_PASS_BOT')
print('EMAIL_USER: ', EMAIL_USER)
print('EMAIL_PASS: ', EMAIL_PASS)

EMAIL_USER:  pt.ogorek.bot@gmail.com
EMAIL_PASS:  goexkonkkzqbmmlz

#! SMTP

# Sending Email

# >>> import smtplib
# >>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
# >>> smtpObj.ehlo()
# (250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
# n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
# >>> smtpObj.starttls()
# (220, b'2.0.0 Ready to start TLS')
# >>> smtpObj.login('bob@example.com', 'MY_SECRET_PASSWORD')
# (235, b'2.7.0 Accepted')
# >>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So
# long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
# {}
# >>> smtpObj.quit()
# (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')

# Connecting to an SMTP Server

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
print(type(smtpObj))
# <class 'smtplib.SMTP'>

smtp_sslObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
print(type(smtp_sslObj))
# <class 'smtplib.SMTP_SSL' >

# Sending the SMTP “Hello” Message
