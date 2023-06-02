from ssl import create_default_context
from smtplib import SMTP_SSL
from os import environ


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "nikhil.23.idiculla@gmail.com"
    password = environ.get("PASSWORD")
    context = create_default_context()
    with SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, username, message)
