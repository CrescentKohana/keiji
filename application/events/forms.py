from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import TextAreaField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.categories import models


class EventForm(FlaskForm):
    category_id = QuerySelectField(
        "Category",
        get_label="name",
        query_factory=lambda: models.Category.query.filter_by(account_id=current_user.id)
    )

    description = TextAreaField(
        "Description",
        [
            validators.Length(min=2, max=2048),
            validators.data_required()
        ]
    )

    duration = IntegerField(
        "Duration (min)",
        [
            validators.number_range(min=1, max=1440, message="Duration must be between %(min)d-%(max)d."),
            validators.data_required(message="Duration must be in whole numbers.")
        ]
    )

    class Meta:
        csrf = False
