import os
import smtplib
from email.message import EmailMessage

from celery import Celery
from config import REDIS_HOST, REDIS_PORT
from dotenv import load_dotenv

load_dotenv()

FASTAPI_USER = os.environ.get('FASTAPI_USER')
FASTAPI_PASS = os.environ.get('FASTAPI_PASS')
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')


def get_email_template(username: str):
    email = EmailMessage()
    email['Subject'] = 'Натрейдил'
    email['From'] = FASTAPI_USER
    email['To'] = FASTAPI_USER
    email.set_content(
        '<h1> test! </h1>'
    )
    return email


@celery.task
def send_email(username: str):
    email = get_email_template(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(FASTAPI_USER, FASTAPI_PASS)
        server.send_message(email)
