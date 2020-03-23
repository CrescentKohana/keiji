from application import db


class Category(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )

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

    onupdate = db.func.current_timestamp()

    account_id = db.Column(
        db.Integer,
        db.ForeignKey('account.id'),
        nullable=False
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description
