from flask import Blueprint, request
from common.decorators import login_required
from .UserController import get_home, get_users


user = Blueprint('user', __name__, template_folder='user_templates',
                 url_prefix='/user',
                 static_folder='static',
                 static_url_path='app/users/static')


@user.route('/<path:path>', methods=["GET", "POST"])
@login_required
def protected(path):
    if path == "home":
        return get_home()
    elif path == "users":
        return get_users()


# @user.route('/confirm_email/<token>')
# def confirm_email(token):
#     return check_token(token)
