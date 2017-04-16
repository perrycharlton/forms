from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect
from frontend.controller import frontend
from users import user
from common.config import BaseConfig, DefaultConfig, INSTANCE_FOLDER_PATH, get_config
csrf = CSRFProtect()

# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    user,
    frontend
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
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_logging(app)
    # configure_login_manager(app)
    # configure_admin(app)

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


def configure_hook(app):
    @app.before_request
    def before_request():
        pass
