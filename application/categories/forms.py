from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators


class CategoryForm(FlaskForm):
    # Minimum in name is only one because some languages such as Japanese can easily have
    # one character long words such as 絵 as in picture.
    name = StringField(
        "Category",
        [
            validators.Length(min=1, max=64),
            validators.data_required()
        ]
    )

    description = TextAreaField(
        "Description",
        [validators.Length(max=1024)]
    )

    class Meta:
        csrf = False
