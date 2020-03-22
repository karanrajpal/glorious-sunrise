import os
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate

def send_email(recipient, subject, body, files=None):
    import smtplib

    user=os.environ['GM_EMAIL']
    pwd = os.environ['GM_APP']
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = ", ".join(TO)
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = SUBJECT

    message.attach(MIMEText(TEXT))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
        # After the file is closed
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
        message.attach(part)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message.as_string())
        server.close()
    except:
        print('failed to send mail')

