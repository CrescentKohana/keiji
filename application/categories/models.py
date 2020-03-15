from application import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # The user who created this category. TODO: Enable after user functionality is added.
    # user_id = db.Column(
    #     db.Integer,
    #     nullable=False
    # )

    date_created = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    name = db.Column(
        db.String(64),
        nullable=False
    )

    description = db.Column(
        db.String(1024),
        nullable=True
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description
