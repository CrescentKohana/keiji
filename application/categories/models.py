from application import db
from application.models import Base


# Link table between categories and clips (many to many).
clip_categories = db.Table(
    'clip_categories',
    db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
    db.Column('clip_id', db.Integer, db.ForeignKey('clip.id'))
)


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
