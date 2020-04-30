from flask import Flask, url_for
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///keiji_data.db"
    app.config["SQLALCHEMY_ECHO"] = True
    # SQLALCHEMY_TRACK_MODIFICATIONS would add significant overhead, so it is disabled.
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)


# User login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."


# Core functionality
from application import views

from application.auth import models
from application.auth import views

from application.categories import models
from application.categories import views

from application.events import models
from application.events import views

from application.clips import models
from application.clips import views

from application.statistics import models
from application.statistics import views


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# If there are any changes in the CSS file,
# these two methods will initiate reloading of the CSS in the browser cache.
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = 'css/style.css'
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


try:
    db.create_all()
except():
    pass
