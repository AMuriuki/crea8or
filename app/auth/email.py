from flask import render_template, current_app
from flask_babel import _
from app.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email(from_email=current_app.config['MAIL_ADMIN'], to_emails=[user.email], 
                subject=_('Creatives - Reset Your Password'), 
                html_content=render_template('email/reset_password.html', user=user, token=token))

