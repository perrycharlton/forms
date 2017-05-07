from flask import Blueprint, request, jsonify
from common.decorators import login_required
from .QuizController import get_quiz, get_home, get_text, update_quiz, upload_file, get_import

quiz = Blueprint('quiz', __name__, template_folder='quiz_templates', url_prefix='/quiz',
                 static_folder='quiz_static',
                 static_url_path='app/quiz/quiz_static')


@quiz.route('/<path:path>', methods=["POST", "GET"])
@login_required
def validate(path):
    if path == "home":
        return get_home()
    elif path == "quiz":
        return get_quiz()
    elif path == "text":
        return get_text()
    elif path == "import":
        return get_import()
    elif path == "upload":
        file = request.files['file']
        print(file)
        data = upload_file(file)
        file.close()

        return data
    elif path == "update":
        content = request.get_json(silent=True, force=True)
        return update_quiz(content)
    elif path == "other.html":
        pass
    elif path == "savequiz":
        # file = request.files['file']
        jsn = request.get_json(force=True)
        test = update_quiz(jsn)
        print(test)

