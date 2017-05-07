from flask import Blueprint, request
from .AuthController import find_user, check_user, signup, check_token, get_home


auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')


@auth.route('/<path:path>', methods=["POST"])
def validate(path):
    if path in ['username', 'email']:
        return find_user(path, request.form[path])
    elif path == 'login':
        return check_user(request.form)
    elif path == 'signup':
        return signup(request.form)


@auth.route('/confirm_email/<token>')
def confirm_email(token):
    return check_token(token)


@auth.route('/<path:path>', methods=["GET"])
def home(path):
    if path == 'home':
        return get_home()
