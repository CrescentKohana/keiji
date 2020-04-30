import datetime
from application import db
from sqlalchemy import text


class Statistics:
    @staticmethod
    def time_spent_on_category(current_user_id):
        query = text("SELECT C.id, C.name, COALESCE(SUM(E.duration),0) "
                     "FROM Category as C "
                     "LEFT JOIN Event as E ON C.id = E.category_id "
                     "WHERE (C.account_id = :user_id) "
                     "GROUP BY C.id "
                     "ORDER BY C.id;",
                     current_user_id).params(user_id=current_user_id)

        result = db.engine.execute(query)

        response = {}
        for item in result:
            response[item[0]] = [item[1], (datetime.timedelta(minutes=(item[2])))]

        return response
