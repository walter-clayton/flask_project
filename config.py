import os

SECRET_KEY = 'H4S6%YI}r,w5#"jya3#<\x0c>gh'

FB_APP_ID = 3084275108271122


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')