from application import db
from application.models import Base


class User(Base):
    __tablename__ = "account"

    nickname = db.Column(db.String(16), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    language = db.Column(db.String(2),   nullable=False)

    categories = db.relationship(
        "Category",
        backref='account',
        lazy=True
    )

    def __init__(self, nickname, username, password, language):
        self.nickname = nickname
        self.username = username
        self.password = password
        self.language = language

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
