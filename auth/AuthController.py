from common import database, mail
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session, g, jsonify, redirect, url_for, render_template
import datetime

import re

users = database.Userdb('users')


def auth_side_menu():
    return {"label": ['home', 'test', 'other'], "link": "auth"}


def check_user(form):
    if not re.match("[^@]+@[^@]+\.[^@]+", form["username"]):
        label = "username"
    else:
        label = "email"

    if users.find_one({label: form["username"]}):
        f_user = users.find_user_details(
            {label: form["username"]},
            {"hash": 1, "email": 1,
             "first_name": 1, "username": 1,
             "email_checked": 1, "admin": 1,
             "_id": 0})
        # temp to stop logging in al the time
        store_user = {
            "first_name": f_user["first_name"],
            "email": f_user["email"],
            "username": f_user["username"]
        }
        if check_password_hash(f_user['hash'], form["password"]) and f_user['email_checked']:
            # user = {"first": f_user["first_name"], "last": f_user['email']}
            session['user'] = store_user

            g.user = store_user
            menus = ['home', 'test', 'other']
            auth_page = {
                "menu": render_template("auth_menu.html", admin=True, user=f_user['first_name']),
                "content": render_template("common_home.html",
                                           side_menu="side_menu.html",
                                           sub_content="auth_info.html",
                                           menus=auth_side_menu()
                                           )
            }
            return jsonify(auth_page)

    print('wrong password')
    html = "Wrong username or password!"
    return jsonify({"message": html})


def signup(form):
    if users.find_one({"username": form["username"]}) == 0:
        if users.find_one({"email": form["email"]}) == 0:
            token = mail.send_mail(form['email'])
            hashed_password = generate_password_hash(form["password"], method='sha256')
            users.create_user(
                {
                    "username": form["username"],
                    "hash": hashed_password,
                    "email": form["email"],
                    "first_name": form["first"],
                    "last_name": form["last"],
                    "email_checked": False,
                    "created_on": datetime.datetime.utcnow(),
                    "token": token,
                    "admin":False
                })

            test = 'Hi ' + form["first"] + ' an email as been sent to ' + form["email"] + \
                   '. Click on the link to continue the registration process?'

            return jsonify({'message': test})
        html = "Email is already being used"
        return jsonify({'message': html})
    html = "Username is already taken"
    return jsonify({'message': html})


def check_token(token):
    confirm = mail.confirmed_email(token)
    # check if the token has expired, if expired re-register, else continue
    if confirm:
        # update user to confirmed
        users.update_user({'token': token}, {'email_checked': True})
        # send user back to front end login page to re login
        return redirect(url_for("frontend.login", start="login"))
    else:
        # if ut took too long to return fails
        html = "The Login has timed out, please try again!"
        return jsonify({"comment": html})


def get_home():
    return jsonify({
        "content": render_template("common_home.html",
                                   side_menu="side_menu.html",
                                   sub_content="auth_info.html",
                                   menus=auth_side_menu()
                                   )
    })


def find_user(label, value):
    # example firm email: perry@perry.com
    return users.find_one({label: value}) == 0