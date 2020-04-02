import datetime
from application import db
from sqlalchemy import text


class Statistics:
    @staticmethod
    def overall_time_spent(current_user_id):
        query = text("SELECT SUM(E.duration) "
                     "FROM Event as E "
                     "LEFT JOIN Category as C ON C.id = E.category_id "
                     "WHERE (C.account_id = :user_id) "
                     "GROUP BY C.account_id;",
                     current_user_id).params(user_id=current_user_id)

        result = db.engine.execute(query)

        return result

    @staticmethod
    def time_spent_on_category(current_user_id):
        query = text("SELECT COALESCE(SUM(E.duration),0) "
                     "FROM Category as C "
                     "LEFT JOIN Event as E ON C.id = E.category_id "
                     "WHERE (C.account_id = :user_id) "
                     "GROUP BY C.id "
                     "ORDER BY C.id;",
                     current_user_id).params(user_id=current_user_id)

        result = db.engine.execute(query)

        response = []
        for item in result:
            response.append(datetime.timedelta(minutes=(item[0] / 60)))

        return response
