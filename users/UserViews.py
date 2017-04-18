from flask import Blueprint, session, redirect, url_for, flash, render_template, g, jsonify
# from .UserForms import LoginForm, SignupForm
from common import data, database

# from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
# from frontend import controller
# from .UserModels import User

user = Blueprint('user', __name__, template_folder='templates',
                 url_prefix='/user',
                 static_folder='static',
                 static_url_path='app/users/static')

users = database.Userdb('users')


@user.route('/user/<path:path>', methods=["GET", "POST"])
def protected(path):
    if g.get('user_id'):
        if path == "protected":

            print(g.get('user_id'))
            return jsonify({"page": render_template("users/protected.html")})
    return redirect(url_for('frontend.index'))

def login(form):
    if users.find_one({"username": form["username"]}):
        f_user = users.find_user_details(
            {"username": form["username"]},
            {"hash": 1, "email": 1, "first_name": 1, "username": 1})
        print(f_user['_id'], 'f-user')
        # if user exits check if password is correct
        if check_password_hash(f_user['hash'], form["password"]):
            flash("Logged in successfully!", category='success')
            session['user_id'] = str(f_user["_id"])
            print(f_user["_id"], 'line 36')
            g.user_id = str(f_user["_id"])
            return protected("protected")

    print('wrong password')
    flash("Wrong username or password!", category='error')

    return redirect(url_for('frontend.index'))


def TrueFalse(condition):
    return "true" if condition else 'false'


def check_username(username):
    user_count = users.find_one({"username": username})
    print('check username', username, user_count)
    print(user_count != 1)

    return TrueFalse(users.find_one({"username": username}) != 1)


def check_email(email):
    return TrueFalse(users.find_one({"username": email}) != 1)


def signup(form):
    if check_username(form["username"]) and check_email(form["email"]):
        hashed_password = generate_password_hash(form["password"], method='sha256')
        user_id = users.create_user(
            {
                "username": form["username"],
                "hash": hashed_password,
                "email": form["email"],
                "first_name": form["first"],
                "last_name": form["last"]})

        test = '<h1>' + form["username"] + ' ' + form["email"] + ' ' + form["password"] + \
               str(user_id) + '</h1>'
        print(test)
        return test
    return redirect(url_for('user.login'))



# @user.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('You were logged out')
#     return redirect(url_for('users/login'))


# @user.route('/settings')
# @login_required
# def settings():
#     return render_template('users/settings.html')





