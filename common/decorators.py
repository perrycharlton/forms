from functools import wraps
from flask import g, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('frontend.login', start='login'))
        return f(*args, **kwargs)
    return decorated_function
