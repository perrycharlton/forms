from flask import render_template, jsonify
from common.random_users import get_users


def admin_side_menu():
    return {"label": ['home', 'admin', 'other'], "link": "admin"}


def get_home():
    side_menu = render_template("side_menu.html", menus=admin_side_menu())
    sub_content = render_template("admin_info.html")

    return jsonify({"side_menu": side_menu, "sub_content": sub_content})


def get_random_users():
    return jsonify({"content": render_template("admin_random_users.html", users=get_users(20))})


