import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '664e2845018cfae983412ed3'
    BCRYPT_LOG_ROUNDS = 20
    BCRYPT_HASH_PREFIX = '2b'
    BCRYPT_HANDLE_LONG_PASSWORDS = False
