import os
import json
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
app = Flask(__name__)
app.config['SECRET_KEY'] = config_srv.get("secret_key")
bootstrap = Bootstrap5(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    print(user_id)
    return session.query(Users).get(user_id)


# --------------   ОБРАБОТЧИКИ   ---------------
@app.route('/login/', methods=['post', 'get'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = session.query(Users).filter(Users.login == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('base'))
        print('form.username.data')
        flash("Invalid username/password", 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.errorhandler(404)
@app.errorhandler(401)
def not_found(error):
    flash(error, category="error")
    msg = 'Ошибка'
    if "401" in str(error):
        msg = 'Пользователь не авторизован (401)'
    elif "404" in str(error):
        msg = 'Страница не найдена (404)'
    return render_template("error404.html", message=msg)


@app.route('/', methods=['GET', 'POST'])
def base():
    return render_template("dot.html")


@app.route('/base')
@login_required
def table_view():
    result = session.execute(
        select(Users)
    ).scalars()
    print(current_user.is_authenticated)
    return render_template("table_view.html", table=result)


# ----------------------------------------------


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host=config_srv.get("host"), port=int(config_srv.get("port")), debug=bool(config_srv.get("debug") == '1'))
