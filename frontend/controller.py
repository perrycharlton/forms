from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from common.data import json_file


frontend = Blueprint('frontend', __name__)


@frontend.route('/')
def index():
    data = json_file('welcome.json')
    return render_template('index.html', data=data)


@frontend.route('/<path:path>', methods=["GET", "POST"])
def login(path):
    if request.method == "GET":
        if path == 'login':
            # login_page = redirect(url_for('user.login'))
            return jsonify({'page': render_template('login.html')})
        elif path == 'signup':
            return jsonify({'page': render_template('signup.html')})

    elif request.method == "POST":
        return redirect(url_for('user.login'), code=307)