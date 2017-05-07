from flask import render_template, jsonify

from common.baconipsum import get_bacon


def get_auth(start):
    content = render_template(start + '.html')
    return jsonify({"content": content})


def get_index():
    bacon = get_bacon(3)
    return render_template("index.html", menu='menu.html', sub_content='bacon.html', data=bacon)


def get_home():
    bacon = get_bacon(3)

    return jsonify({"content": render_template('bacon.html', data=bacon)})


def get_logout():
    bacon = get_bacon(3)

    menu = render_template('menu.html')
    content = render_template('bacon.html', data=bacon)
    return jsonify({"content": content, 'menu': menu})
