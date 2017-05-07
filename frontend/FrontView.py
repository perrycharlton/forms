from flask import Blueprint, jsonify
from .controller import get_home, get_auth, get_logout, get_index
from common.decorators import login_required

frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    return get_index()


@frontend.route('/<start>', methods=["GET"])
def login(start):
    if start in ['login', 'signup']:
        return get_auth(start)
    if start == 'home':
        return get_home()


@frontend.route('/logout', methods=["GET"])
@login_required
def logout():
    return get_logout()
