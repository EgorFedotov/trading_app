from email.message import EmailMessage
import smtplib
from celery import Celery

FASTAPI_USER = 'egorfedotovarz@gmail.com'
FASTAPI_PASS = 'wfnuhrudtyqkgrck'
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker='redis://localhost:6379')
# celery.broker_connection()


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил'
    email['From'] = FASTAPI_USER
    email['To'] = FASTAPI_USER
    email.set_content(
        '<h1> test! </h1>'
    )
    return email


# @celery.task
def send_email(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(FASTAPI_USER, FASTAPI_PASS)
        server.send_message(email)
