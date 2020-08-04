import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://sakshi:sakshi23@localhost:3306/gutendb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
