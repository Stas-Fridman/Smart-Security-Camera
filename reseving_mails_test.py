import imaplib
import email
from email.header import decode_header
import mail


def receiving_mail():
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    username = 'YOUR EMAIL'
    password = 'YOUR PASSWORD'
    imap.login(username, password)
    status, messages = imap.select("INBOX")
    N = 2
    messages = int(messages[0])
    # going from the top to the bottom, the newest email messages got the highest id number
    for i in range(messages, messages - N, -1):
        # fetches the email message by ID using the standard format specified in RFC 822.
        res, msg = imap.fetch(str(i), "(RFC822)")
        for response in msg:
            if isinstance(response, tuple):
                # parse a bytes email into a message object
                msg = email.message_from_bytes(response[1])
                # decode the email subject
                subject = decode_header(msg["Subject"])[0][0]
                if isinstance(subject, bytes):
                    # if it's a bytes, decode to str
                    subject = subject.decode()
                # email sender
                from_ = msg.get("From")
                if str(from_) == " <email> ":
                    print("From:", from_)
                    print("Subject:", subject)
                    mail.SUB = str(subject)
                    mail.FROM = str(from_)
                    # iterate over email parts
                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))
                        try:
                            # get the email body
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                        if content_type == "text/plain" and "attachment" not in content_disposition:
                            mail.BODY = str(body)
                            return True

    imap.close()
    imap.logout()
