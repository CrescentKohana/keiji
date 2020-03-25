from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, validators


class LoginForm(FlaskForm):
    username = StringField("Username", [validators.data_required()])
    password = PasswordField("Password", [validators.data_required()])

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    nickname = StringField("Nickname", [validators.Length(min=3), validators.data_required()])
    username = StringField("Username", [validators.Length(min=3), validators.data_required()])
    password = PasswordField("Password", [validators.Length(min=8), validators.data_required()])
    language = SelectField(
        "Language",
        [validators.Length(min=2), validators.data_required()],
        choices=[('en', 'English'), ('fi', 'Finnish'), ('jp', 'Japanese')]
    )

    class Meta:
        csrf = False
