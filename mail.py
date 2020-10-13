import smtplib
from email.message import EmailMessage
import imghdr

SUB = ''
FROM = ''
BODY = ''


def mail_sender():
    # email address
    EMAIL_ADDRESS = 'YOUR EMAIL'
    # password
    EMAIL_PASSWORD = 'EMAIL PASSWORD'
    # Contact List
    contacts = ['EMAIL', "ANOTHER EMAIL"]

    msg = EmailMessage()
    msg['Subject'] = 'secure system'
    # the sender's email address
    msg['From'] = EMAIL_ADDRESS
    # the list of all recipients' email addresses
    msg['To'] = ', '.join(contacts)
    msg.set_content('its works')

    files = ['intruder.jpg']

    for file in files:
        # Call open(file, mode) with the desired file as file and "rb" as mode to open the binary file.
        with open(file, 'rb') as file_:
            file_data = file_.read()
            # for an image
            file_type = imghdr.what(file_.name)
            file_name = file_.name
            # for different files you need different main type and subtype
            msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

    # Send the email via our own SMTP server.
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # login in function
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        print('logged in securely')
        smtp.send_message(msg)
        print('all good the mail has been sent')
