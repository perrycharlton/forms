from flask import Blueprint, render_template, redirect, url_for, flash
# from .UserForms import LoginForm, SignupForm
from common import data, database
# from flask_login import login_user, logout_user, login_required, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from frontend import controller
# from .UserModels import User


user = Blueprint('user', __name__, template_folder='templates',
                 url_prefix='/user',
                 static_folder='static',
                 static_url_path='app/users/static')

#
# def login():
#     print('your at the correct place')

    # print('form errors 27', form.username.data, form.password.data)
    # if form.validate_on_submit():
    #     print('validated correctly')
    #     database.db_user = database.Userdb('user')
    #
    #     if database.db_user.find_one({"username": form.username.data}):
    #         f_user = database.db_user.find_user_details(
    #             {"username": form.username.data},
    #             {"hash": 1, "email": 1, "first_name": 1, "username": 1})
    #         print(f_user, 'f-user')
    #         # if user exits check if password is correct
    #         if check_password_hash(f_user['hash'], form.password.data):
    #             user_obj = User(f_user)
    #             # session['logged_in'] = True
    #             # login_user(user_obj)
    #             flash("Logged in successfully!", category='success')
    #         return redirect(url_for('users.index'))
    #     flash("Wrong username or password!", category='error')
    # print(form.errors, 'form errors 45', controller.csrf)
    # return render_template('users/login.html')


# def signup():
    # form = SignupForm()
    # if form.validate_on_submit():
        # # user = app.config['USERS_COLLECTION']
        # if app.config['USERS_COLLECTION'].find_one(
        #         {'$or': [{"username": form.username.data},
        #                  {"email": form.email.data}]}) != 1:
        #
        #     hashed_password = generate_password_hash(form.password.data, method='sha256')
        #     user_id = app.config['USERS_COLLECTION'].insert_one(
        #         {"username": form.username.data, "hash": hashed_password, "email": form.email.data,
        #          "first_name": form.username.data, "last_name": form.last_name.data})
        #
        #     return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + \
        #            str(user_id.inserted_id) + '</h1>'
        # return redirect(url_for('user.login'))



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





