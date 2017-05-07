from common.data import quiz_json_file, quiz_json_to_file
from flask import jsonify, render_template, g
from common.import_to_json import import_file, import_stream
from common.helpers import strip_whitespace
from quiz import quiz_tests
from werkzeug.utils import secure_filename
import os


def quiz_side_menu():
    return {"label": ['home', 'quiz', 'import', 'other'],
            "link": "quiz",
            "js_file": "js/quiz.js"
            }


def get_quiz():
    menus = {"label": ['home',  'results', 'shuffle'],
             "link": "quiz",
             "js_file": "js/quiz.js"
             }
    file_name = "201"
    quiz = quiz_tests.get_tests({'unit': file_name})
    title = quiz['title']
    unit = quiz['unit']
    questions = quiz['questions']
    # this will be used to show no off questions flaged etc
    side_menu = render_template("side_menu.html", menus=menus)
    sub_content = render_template("quiz_page.html", title=title, unit=unit)
    return jsonify({
        'questions': questions,
        'side_menu': side_menu,
        'sub_content': sub_content,
        'unit': unit,
        'user': g.user
    })


def get_home():
    f_list = []
    files = os.listdir("quiz/quiz_static/data")
    for file in files:
        f_list.append(file.split('.')[0])

    print(f_list)
    side_menu = render_template("side_menu.html", menus=quiz_side_menu())
    sub_content = render_template("quiz_info.html", quizzes=files, units=sorted(f_list))

    return jsonify({"side_menu": side_menu, "sub_content": sub_content})


def get_start():
    menus = ['home', 'quiz', 'import', 'other']
    side_menu = "side_menu.html"
    info = "quiz_info.html"
    content = render_template("common_home.html", side_menu=side_menu, sub_content=info, menus=menus)
    return jsonify({'content': content})


def get_text(file=""):
    file = "2365_02_l2_201_sample_questions_and_answers.doc"

    return jsonify(import_file(file))


def update_quiz(data):
    strip_whitespace(data)
    images = data.pop('images', None)
    quiz_tests.save_images(images)
    quiz_tests.save_tests(data)
    # quiz_json_to_file({"questions": data}, 'unit201.json')
    return "worked"


def upload_file(file):
    file_name = secure_filename(file.filename)
    file_ext = file_name.split('.')[1]
    print(file_name, file_ext)

    if file_ext == "txt":
        test_file = file.read()
        test_file = test_file.decode("utf-8")
        data = import_stream(test_file)
        # quiz_tests.save_tests(data)
        # return jsonify(data)

        sub_content = render_template('quiz_edit.html', data=data)
        return jsonify({'sub_content': sub_content})
    else:
        return jsonify({"message": "Only txt files are allowed?"})


def get_import():
    sub_content = render_template("quiz_upload.html")
    return jsonify({'sub_content': sub_content})