class Config(object):
    SECRET_KEY = 'secret key'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/app'

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_ECHO = True