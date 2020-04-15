from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.categories import models


class ClipForm(FlaskForm):
    category_id = QuerySelectField(
        "Category",
        get_label="name",
        query_factory=lambda: models.Category.query.filter_by(account_id=current_user.id)
    )

    content = TextAreaField(
        "Content",
        [
            validators.Length(min=2, max=4096),
            validators.data_required()
        ]
    )

    class Meta:
        csrf = False
