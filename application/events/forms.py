from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.categories import models


class EventForm(FlaskForm):
    category_id = QuerySelectField(
        "Category",
        get_label="name",
        query_factory=lambda: models.Category.query
    )

    description = TextAreaField(
        "Description",
        [validators.Length(min=2), validators.data_required()]
    )

    duration = IntegerField(
        "Duration",
        [
            validators.number_range(min=1, max=86400, message="Minimum for the duration is 1s and maximum is 24h."),
            validators.data_required()
        ]
    )

    class Meta:
        csrf = False
