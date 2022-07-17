# 18 SENDING EMAIL AND TEXT MESSAGES

#! ezgmail - doesn't work - oudated?
# import ezgmail
# import os
# # os.chdir(r'D:\PROGRAMOWANIE\GIT\school\sweigart_automate\credentials.json')
# os.chdir(r'/mnt/d/PROGRAMOWANIE/GIT/school/sweigart_automate')
# ezgmail.init()

import pyzmail
import imaplib
import pprint
import imapclient
import os

import smtplib
EMAIL_USER = os.environ.get('EMAIL_USER_BOT')
EMAIL_PASS = os.environ.get('EMAIL_PASS_BOT')
# print('EMAIL_USER: ', EMAIL_USER)
# print('EMAIL_PASS: ', EMAIL_PASS)


#! SMTP

# ? Sending Email

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

# # ? Connecting to an SMTP Server

# smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
# print(type(smtpObj))
# # <class 'smtplib.SMTP'>

# # smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# # print(type(smtpObj))
# # # <class 'smtplib.SMTP_SSL' >

# # ? Sending the SMTP “Hello” Message

# print(smtpObj.ehlo())
# # (250, b'smtp.gmail.com at your service, [194.177.28.189]\nSIZE 35882577\n8BITMIME\nAUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')

# # ? Starting TLS Encryption

# print(smtpObj.starttls())
# # (220, b'2.0.0 Ready to start TLS')

# # ? Logging In to the SMTP Server

# print(smtpObj.login(EMAIL_USER, EMAIL_PASS))
# # (235, b'2.7.0 Accepted')

# # ? Sending an Email

# print(smtpObj.sendmail(
#     EMAIL_USER,
#     ['pt.ogorek.test@gmail.com', 'pt.ogorek.bot@gmail.com'],
#     'Subject: So long.\nDear Alice, so long and thanks for all the fish.Sincerely, Bob'))
# # {}

# # Disconnecting from the SMTP Server

# print(smtpObj.quit())

#! IMAP

# ? Retrieving and Deleting Emails with IMAP

# import imapclient
# >>> imapObj = imapclient.IMAPClient('imap.example.com', ssl=True)
# >>> imapObj.login('my_email_address@example.com', 'MY_SECRET_PASSWORD')
# # 'my_email_address@example.com Jane Doe authenticated (Success)'
# >>> imapObj.select_folder('INBOX', readonly=True)
# >>> UIDs = imapObj.search(['SINCE 05-Jul-2019'])
# >>> UIDs
# # [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
# >>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
# >>> import pyzmail
# >>> message = pyzmail.PyzMessage.factory(rawMessages[40041][b'BODY[]'])
# >>> message.get_subject()
# # 'Hello!'
# >>> message.get_addresses('from')
# # [('Edward Snowden', 'esnowden@nsa.gov')]
# >>> message.get_addresses('to')
# # [('Jane Doe', 'jdoe@example.com')]
# >>> message.get_addresses('cc')
# # []
# >>> message.get_addresses('bcc')
# # []
# >>> message.text_part != None
# # True
# >>> message.text_part.get_payload().decode(message.text_part.charset)
# # 'Follow the money.\r\n\r\n-Ed\r\n'
# >>> message.html_part != None
# # True
# >>> message.html_part.get_payload().decode(message.html_part.charset)
#
## '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'
# >>> imapObj.logout()

# ? Connecting to an IMAP Server

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# ? Logging In to the IMAP Server

imapObj.login(EMAIL_USER, EMAIL_PASS)
# b'pt.ogorek.bot@gmail.com authenticated (Success)'

# ? Searching for Email

# Selecting a Folder

pprint.pprint(imapObj.list_folders())
# [((b'\\HasNoChildren',), b'/', 'INBOX'),
#  ((b'\\HasChildren', b'\\Noselect'), b'/', '[Gmail]'),
#  ((b'\\All', b'\\HasNoChildren'), b'/', '[Gmail]/All Mail'),
#  ((b'\\Drafts', b'\\HasNoChildren'), b'/', '[Gmail]/Drafts'),
#  ((b'\\HasNoChildren', b'\\Important'), b'/', '[Gmail]/Important'),
#  ((b'\\HasNoChildren', b'\\Sent'), b'/', '[Gmail]/Sent Mail'),
#  ((b'\\HasNoChildren', b'\\Junk'), b'/', '[Gmail]/Spam'),
#  ((b'\\Flagged', b'\\HasNoChildren'), b'/', '[Gmail]/Starred'),
#  ((b'\\HasNoChildren', b'\\Trash'), b'/', '[Gmail]/Trash')]


imapObj.select_folder('INBOX', readonly=True)

# ? Performing the Search

# UIDs = imapObj.search(['SINCE 05-Jul-2019']) # Doesn't work
UIDs = imapObj.search(['ALL'])
print(UIDs)
# [40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]

# ? Size Limits

imaplib._MAXLINE = 10000000

# ? Fetching an Email and Marking It as Read

rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
pprint.pprint(rawMessages)

imapObj.select_folder('INBOX', readonly=False)

# ? Getting Email Addresses from a Raw Message

message = pyzmail.PyzMessage.factory(rawMessages[2][b'BODY[]'])


message.get_subject()
# 'Hello!'
print(message.get_addresses('from'))
# [('Edward Snowden', 'esnowden@nsa.gov')]
print(message.get_addresses('to'))
# [('Jane Doe', 'my_email_address@example.com')]
message.get_addresses('cc')
# []
message.get_addresses('bcc')
# []

# ? Getting the Body from a Raw Message

message.text_part != None
# True
message.text_part.get_payload().decode(message.text_part.charset)
# 'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
message.html_part != None
# True
message.html_part.get_payload().decode(message.html_part.charset)
# '<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'

# ? Deleting Emails

imapObj.select_folder('INBOX', readonly=False)
UIDs = imapObj.search(['ON 09-Jul-2019'])
UIDs
# [40066]
imapObj.delete_messages(UIDs)
# {40066: ('\\Seen', '\\Deleted')}
imapObj.expunge()
# ('Success', [(5452, 'EXISTS')])

# ? Disconnecting from the IMAP Server
imapObj.logout()

# ? Sending Text Messages with Twilio

# Didn't start - only for usa
