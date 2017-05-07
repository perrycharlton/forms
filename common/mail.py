from flask_mail import Message
from flask import url_for
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadTimeSignature
from config import BaseConfig
import myproject

safe = URLSafeTimedSerializer(BaseConfig.SECRET_KEY)


def send_mail(email):
    token = safe.dumps(email)
    msg = Message('confirm Email', sender='perry@perrycharlton.com', recipients=[email])
    link = url_for('user.confirm_email', token=token, _external=True)
    msg.body = 'Your link is {}'.format(link)
    myproject.mail.send(msg)
    return token


def confirmed_email(token):

        # email = safe.loads(token, max_age=1800)
    sig_okay, email = safe.loads_unsafe(token, max_age=1800)
    print(email, "line 22, mail.py", sig_okay)
    return sig_okay


