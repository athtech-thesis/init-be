from services.email.email_template import INIT_HTML_EMAIL
from dotenv import load_dotenv

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import smtplib
import os

load_dotenv()

def send_verification_email(username, email, token):
    init_no_info = os.getenv('INFO_EMAIL')
    user = email
    user_name = username
    verification_link = os.getenv('CLIENT_VERIFICATION_LINK').format(token=token)
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Verification Link For init.io"
    msg['From'] = init_no_info
    msg['To'] = user

    html = INIT_HTML_EMAIL.format(user_name=user_name, verification_link=verification_link, app_name=os.getenv('APP_NAME'))

    # Record the MIME types of both parts - text/plain and text/html.
    # part1 = MIMEText(text, 'plain')
    html_part = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    # msg.attach(part1)
    msg.attach(html_part)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', os.getenv('EMAIL_PORT'))

    mail.ehlo()

    mail.starttls()
    mail.login('init.info.athtech@gmail.com', 'initinfo1234')
    mail.sendmail(init_no_info, user, msg.as_string())
    mail.quit()