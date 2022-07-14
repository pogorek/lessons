# import os
# import smtplib
# import imghdr
# from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# contacts = ['YourAddress@gmail.com', 'test@example.com']

# msg = EmailMessage()
# msg['Subject'] = 'Check out Bronx as a puppy!'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'YourAddress@gmail.com'

# msg.set_content('This is a plain text email')

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)

# ==================================================
# With attachment

import os
import smtplib  # Lib for sending emails
import ssl  # Lib for secure SSL context
import imghdr  # For image files to check file type
from email.message import EmailMessage  # Lib for formatting message

# Get login and pass from env vars
EMAIL_ADDRESS = os.environ.get('EMAIL_USER_BOT')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS_BOT')

# Create a secure SSL context
context = ssl.create_default_context()

# List of recipients
contacts = ['pt.ogorek.test@gmail.com']

# Create EmailMessage object and add required fields
msg = EmailMessage()
msg['Subject'] = 'Check out image!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = contacts

# Add plaintext email body
msg.set_content('MARTA IMG attached. Enjoy!!')

# Add html email body
msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">MARTA IMG attached. Enjoy!!</h1>
    </body>
</html>
""", subtype='html')

# For jpg files

# List of files to attach
files = ['marta.jpg', 'marta2.jpg']

# Loop for each file
for file in files:
    # Open file
    with open(file, 'rb') as f:
        file_data = f.read()  # Read image data
        file_type = imghdr.what(f.name)  # Check type of image
        file_name = f.name  # Get name of the file

    # Add attachment to message
    msg.add_attachment(file_data, maintype='image',
                       subtype=file_type, filename=file_name)

# # For pdf files

# # List of files to attach
# files = ['testfile.pdf']

# # Loop for each file
# for file in files:
#     # Open file
#     with open(file, 'rb') as f:
#         file_data = f.read()  # Read image data
#         # file_type = imghdr.what(f.name)  # Check type of image
#         file_name = f.name  # Get name of the file

#     # Add attachment to message
#     msg.add_attachment(file_data, maintype='application',
#                        subtype='octet-stream', filename=file_name)


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


# ==================================================
# My version

# import os
# import smtplib
# import imghdr
# from email.message import EmailMessage

# EMAIL_ADDRESS = os.environ.get('EMAIL_USER_BOT')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS_BOT')

# # contacts = ['YourAddress@gmail.com', 'test@example.com']

# msg = EmailMessage()
# msg['Subject'] = 'Check out first email try!'
# msg['From'] = EMAIL_ADDRESS
# msg['To'] = 'pt.ogorek.test@gmail.com'

# msg.set_content('This is a plain text email')

# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')

# with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)
