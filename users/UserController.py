from flask import render_template, jsonify
from common.random_users import get_users


def user_side_menu():
    return {"label": ['home', 'users', 'other'], "link": "user"}


def get_home():
    side_menu = render_template("side_menu.html", menus=user_side_menu())
    sub_content = render_template("user_info.html")

    return jsonify({"side_menu": side_menu, "sub_content": sub_content})



def get_users():
    return jsonify({"page": render_template("users_random.html", users=get_users(20))})
