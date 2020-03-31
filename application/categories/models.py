from application import db
from application.models import Base


class Category(Base):
    name = db.Column(
        db.String(64),
        nullable=False
    )

    description = db.Column(
        db.String(1024),
        nullable=True
    )

    account_id = db.Column(
        db.Integer,
        db.ForeignKey('account.id'),
        nullable=False
    )

    def __init__(self, name, description):
        self.name = name
        self.description = description
