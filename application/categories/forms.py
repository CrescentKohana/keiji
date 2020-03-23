from flask_wtf import FlaskForm
from wtforms import StringField, validators


class CategoryForm(FlaskForm):
    # Minimum in name is only one because some languages such as Japanese can easily have
    # one character long words such as 絵 as in picture.
    name = StringField("Category name", [validators.Length(min=1)])
    description = StringField("Description", [validators.Length(min=3)])

    class Meta:
        csrf = False
