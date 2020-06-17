from threading import Thread
from flask import current_app
from flask_mail import Message
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
# from app import mail


def send_async_email(app, msg):
    with app.app_context():
        sg = SendGridAPIClient(app.config['SENDGRID_API_KEY'])
        response = sg.send(msg)
        print(response.status_code)
        print(response.body)
        print(response.headers)       


def send_email(from_email, to_emails, subject, html_content):
    msg = Mail(from_email=from_email, to_emails=to_emails, subject=subject, html_content=html_content)
    Thread(target=send_async_email,
            args=(current_app._get_current_object(), msg)).start()
