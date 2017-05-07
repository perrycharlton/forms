from flask import Flask, g, session
import os
from flask_wtf.csrf import CSRFProtect
from frontend.FrontView import frontend
from users.UserViews import user
from admin.AdminView import admin
from quiz.QuizView import quiz
from auth.AuthView import auth
from common.config import BaseConfig, DefaultConfig, INSTANCE_FOLDER_PATH, get_config
from flask_mail import Mail
import passwords
# import flask_login
csrf = CSRFProtect()


mail = Mail()
# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    user,
    frontend,
    admin,
    quiz,
    auth
]


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        print(DefaultConfig.PROJECT)
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS
    if config is None:
        b_config = BaseConfig()
        config = b_config

    app = Flask(app_name, instance_path=INSTANCE_FOLDER_PATH, instance_relative_config=True)
    csrf.init_app(app)
    config_mail(app)
    # login_manager.init_app(app)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_logging(app)

    return app


def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    if config:
        app.config.from_object(config)
        return

    # get mode from os environment
    application_mode = os.getenv('APPLICATION_MODE', 'LOCAL')
    app.config.from_object(get_config(application_mode))


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_logging(app):
    pass


def config_mail(app):
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = passwords.EMAIL_USERNAME
    app.config['MAIL_PASSWORD'] = passwords.EMAIL_PASSWORD
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEFAULT_SENDER '] = passwords.EMAIL_USERNAME
    mail = Mail(app)
    # return mail



def configure_hook(app):
    @app.before_request
    def before_request():
        if session.get('user'):
            g.user = session.get('user')
        else:
            g.user = None
        pass
