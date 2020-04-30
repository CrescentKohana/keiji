from flask import redirect, render_template, request, url_for
from flask_login import login_user, logout_user, login_required, current_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm, SettingsForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user or not user.check_password(form.password.data):
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form=RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/registerform.html", form=form)

    if User.query.filter(User.username == form.username.data):
        form.username.errors.append("This username already exists.")
        return render_template("auth/registerform.html", form=form)

    u = User(form.nickname.data, form.username.data, form.password.data, form.language.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/settings", methods=["GET"])
@login_required
def settings_view():
    return render_template(
        "auth/settings.html",
        user=User.query.filter(User.id == current_user.id).first(),
        form=SettingsForm()
    )


@app.route("/auth/settings", methods=["POST"])
@login_required
def user_edit():
    form = SettingsForm(request.form)
    c = User.query.get(current_user.id)

    if not form.password.data:
        form.password.data = c.password

    if not form.validate():
        return render_template(
            "auth/settings.html",
            user=User.query.filter(User.id == current_user.id).first(),
            form=form
        )

    c.nickname = form.nickname.data
    c.password = form.password.data
    c.language = form.language.data

    db.session().commit()

    return redirect("/")
