import os
from pa_messenger import get_env


class DefaultConfig(object):
    SECRET_KEY = 'youshouldreallychangethis'
    DEBUG = False
    CURR_PATH = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + CURR_PATH + '/../mews.db')
    TWILIO_ACCOUNT_SID = 'Put your twilio account sid here'
    TWILIO_AUTH_TOKEN = 'Put your twilio auth token here'
    TWILIO_NUMBER = '+15031234567'
    SUBSCRIBE_COMMAND = 'join'
    UNSUBSCRIBE_COMMAND = 'stop'
    BASIC_AUTH_USERNAME = 'admin'
    BASIC_AUTH_PASSWORD = 'SoSecret'


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    CURR_PATH = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + CURR_PATH + '/../mews_dev.db')


class TestConfig(DefaultConfig):
    CURR_PATH = os.path.dirname(os.path.realpath(__file__))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///' + CURR_PATH + '/../mews_test.db')

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


config_env_files = {
    'test': 'pa_messenger.config.TestConfig',
    'development': 'pa_messenger.config.DevelopmentConfig',
}

