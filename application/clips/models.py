from application import db
from application.models import Base
from application.categories.models import clip_categories

from sqlalchemy import text


class Clip(Base):
    content = db.Column(
        db.String(4096),
        nullable=False
    )

    categories = db.relationship(
        'Category',
        secondary=clip_categories,
        backref=db.backref('bref', lazy='dynamic')
    )

    def __repr__(self):
        return str(self.id)

    def __init__(self, categories, content):
        self.categories = categories
        self.content = content

    @staticmethod
    def find_clips_user_has_permissions_to(current_user_id):
        query = text("SELECT CL.id, CL.date_created, CL.date_modified, CL.content, CC.category_id "
                     "FROM Clip AS CL "
                     "JOIN clip_categories CC "
                     "ON CL.id = CC.clip_id "
                     "JOIN Category AS C ON C.id = CC.category_id AND C.account_id = :user_id "
                     "GROUP BY CL.id, CL.date_created, CL.date_modified, CL.content, CC.category_id",
                     current_user_id).params(user_id=current_user_id)

        return db.engine.execute(query)

    @staticmethod
    def get_clip_owner(clip_id):
        db.relationship("C")
        query = text("SELECT C.account_id "
                     "FROM Category as C "
                     "WHERE C.id = (SELECT CC.category_id FROM clip_categories CC WHERE CC.clip_id = :clid LIMIT 1) "
                     "GROUP BY C.account_id ",
                     clip_id).params(clid=clip_id)

        return db.engine.execute(query).first().items()[0][1]
