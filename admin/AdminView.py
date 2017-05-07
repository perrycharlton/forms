from flask import Blueprint
from common.decorators import login_required
from .AdminController import get_home, get_random_users

admin = Blueprint('admin', __name__, template_folder='admin_templates',
                  url_prefix='/admin',
                  static_folder='static',
                  static_url_path='app/admin/static')


@admin.route('/<path:path>', methods=["POST", "GET"])
@login_required
def validate(path):
    if path == "home":
        return get_home()
    elif path == "other.html":
        pass

    # elif path == 'gen_user.html':
    #     users = get_users(5)
    #     return jsonify({'page': render_template('random_users.html', users=users)})