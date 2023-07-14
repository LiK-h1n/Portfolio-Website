from ssl import create_default_context
from smtplib import SMTP_SSL


def send_email(message, username, password):
    host = "smtp.gmail.com"
    port = 465
    context = create_default_context()
    with SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
