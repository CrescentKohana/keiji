from application import db


class Event(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )

    date_created = db.Column(
        db.DateTime,
        default=db.func.current_timestamp()
    )

    date_modified = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    description = db.Column(
        db.String(2048),
        nullable=True
    )

    duration = db.Column(
        db.Integer,
        nullable=False
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        nullable=False
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey('account.id'),
        nullable=False
    )

    def __repr__(self):
        return str(self.id)

    def __init__(self, category_id, duration, description):
        self.category_id = category_id
        self.duration = duration
        self.description = description
