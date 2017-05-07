import os
from pymongo import MongoClient
import passwords

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')


class BaseConfig(object):
    PROJECT = "app"

    # Get app root path, also can use flask.root_path.
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    DEBUG = False
    TESTING = False

    ADMINS = [passwords.EMAIL_USERNAME]

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = os.urandom(24)

    MONGOD_DATABASE_URI = MongoClient(passwords.SERVER_ADDRESS + ':27017')

    DB_NAME = 'Users'

    DATABASE = MONGOD_DATABASE_URI[DB_NAME]

    USERS_COLLECTION = DATABASE.users

    EXPLAIN_TEMPLATE_LOADING = False


class DefaultConfig(BaseConfig):
    # Statement for enabling the development environment
    DEBUG = True


class LocalConfig(DefaultConfig):
    # config for local development
    pass


class StagingConfig(DefaultConfig):
    # config for staging environment
    pass


class ProdConfig(DefaultConfig):
    # config for production environment
    pass


def get_config(MODE):
    SWITCH = {
        'LOCAL': LocalConfig,
        'STAGING': StagingConfig,
        'PRODUCTION': ProdConfig
    }
    return SWITCH[MODE]