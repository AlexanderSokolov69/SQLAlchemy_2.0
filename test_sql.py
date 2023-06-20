import os
import json
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from classes import *

import sys
import sqlalchemy

from flask import Flask, g, request, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager, current_user, login_required, login_user

from forms.f_login import LoginForm

# My base structure
# Back up the reference to the exceptionhook

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

# DBsession = sqlalchemy.orm.sessionmaker(bind=engine)
# session = DBsession()
with open("config_srv.json", "r", encoding="utf-8") as f:
    config_srv = json.load(f)

session = init_db(config_srv.get("connect_str"), echo=bool(config_srv.get("debug") == '1'))


if __name__ == '__main__':
    with session as s:
        users = s.query(Users).all()
        for user in users:
            if len(user.login.strip()) > 0:
                if user.login.strip() == 'sa':
                    psw = '030669'
                else:
                    psw = user.login.upper()
                user.passwd = generate_password_hash(psw)
                print(user.login.strip(), '\t', user.passwd)
        s.commit()
        # psw = 'MOA'
        # user.passwd = generate_password_hash(psw)
        # s.commit()
        # print(user)
        