"""
This one:
https://www.thepythoncode.com/article/use-gmail-api-in-python

Additional:
https://www.thepythoncode.com/article/sending-emails-in-python-smtplib
https://www.thepythoncode.com/article/reading-emails-in-python
https://www.thepythoncode.com/article/deleting-emails-in-python
https://likegeeks.com/python-send-emails/
"""

import os
import pickle
# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode
# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from mimetypes import guess_type as guess_mime_type

# Request all access (permission to read/send/receive emails, manage the inbox, and more)
SCOPES = ['https://mail.google.com/']
our_email = 'pt.ogorek.bot@gmail.com'


# ? Function that loads the credentials.json, does the authentication with Gmail API and returns a service object that can be used later in all in our upcoming functions:

def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)


# get the Gmail API service
service = gmail_authenticate()

#! Sending Emails

# ? First, let's start with the function that sends emails, we know that emails can contain attachments, so we will define a function that adds an attachment to a message, a message is an instance of MIMEMultipart (or MIMEText, if it doesn't contain attachments):

# Adds the attachment with the given filename to the given message


def add_attachment(message, filename):
    content_type, encoding = guess_mime_type(filename)
    if content_type is None or encoding is not None:
        content_type = 'application/octet-stream'
    main_type, sub_type = content_type.split('/', 1)
    if main_type == 'text':
        fp = open(filename, 'rb')
        msg = MIMEText(fp.read().decode(), _subtype=sub_type)
        fp.close()
    elif main_type == 'image':
        fp = open(filename, 'rb')
        msg = MIMEImage(fp.read(), _subtype=sub_type)
        fp.close()
    elif main_type == 'audio':
        fp = open(filename, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=sub_type)
        fp.close()
    else:
        fp = open(filename, 'rb')
        msg = MIMEBase(main_type, sub_type)
        msg.set_payload(fp.read())
        fp.close()
    filename = os.path.basename(filename)
    msg.add_header('Content-Disposition', 'attachment', filename=filename)
    message.attach(msg)

# ? Second, we write a function that takes some message parameters, builds, and returns an email message:


def build_message(destination, obj, body, attachments=[]):
    if not attachments:  # no attachments given
        message = MIMEText(body)
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
    else:
        message = MIMEMultipart()
        message['to'] = destination
        message['from'] = our_email
        message['subject'] = obj
        message.attach(MIMEText(body))
        for filename in attachments:
            add_attachment(message, filename)
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}


# ? And finally, we make a function that takes message parameters, uses the Google mail API to send a message constructed with the build_message() we previously defined:

def send_message(service, destination, obj, body, attachments=[]):
    return service.users().messages().send(
        userId="me",
        body=build_message(destination, obj, body, attachments)
    ).execute()


# test send email #! PDF was corupted in recipients inbox
# send_message(service, "pt.ogorek.test@gmail.com", "This is a TEST subject",
#              "This is the body of the TEST email", ["marta.jpg", "testfile.pdf"])

#! Reading Emails
...
