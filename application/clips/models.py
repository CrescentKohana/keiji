from application import db
from application.models import Base

from sqlalchemy import text


class Clip(Base):
    content = db.Column(
        db.String(4096),
        nullable=True
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey('category.id'),
        nullable=False
    )

    def __repr__(self):
        return str(self.id)

    def __init__(self, category_id, content):
        self.category_id = category_id
        self.content = content

    @staticmethod
    def find_clips_user_has_permissions_to(current_user_id):
        query = text("SELECT CL.id, CL.date_created, CL.date_modified, CL.content, CL.category_id "
                     "FROM Clip as CL "
                     "LEFT JOIN Category as C "
                     "ON C.id = CL.category_id "
                     "WHERE (C.account_id = :user_id) "
                     "GROUP BY CL.id",
                     current_user_id).params(user_id=current_user_id)

        return db.engine.execute(query)

    @staticmethod
    def get_clip_owner(clip_id):
        query = text("SELECT C.account_id "
                     "FROM Category as C "
                     "LEFT JOIN Clip as CL "
                     "ON C.id = CL.category_id "
                     "WHERE (CL.id = :clid) "
                     "GROUP BY CL.id",
                     clip_id).params(clid=clip_id)

        return db.engine.execute(query).first().items()[0][1]
