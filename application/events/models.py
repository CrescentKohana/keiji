from application import db
from application.models import Base

from sqlalchemy import text


class Event(Base):
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

    def __repr__(self):
        return str(self.id)

    def __init__(self, category_id, duration, description):
        self.category_id = category_id
        self.duration = duration
        self.description = description

    @staticmethod
    def find_events_user_has_permissions_to(current_user_id):
        query = text("SELECT E.id, E.date_created, E.date_modified, E.description, E.duration, E.category_id "
                     "FROM Event as E "
                     "LEFT JOIN Category as C "
                     "ON C.id = E.category_id "
                     "WHERE (C.account_id = :user_id) "
                     "GROUP BY E.id",
                     current_user_id).params(user_id=current_user_id)

        result = db.engine.execute(query)

        return result
