import datetime

from flask import render_template
from flask_login import login_required, current_user

from application import app

from application.statistics.models import Statistics
from application.categories.models import Category
from application.events.models import Event

from application.categories.forms import CategoryForm


@app.route("/statistics", methods=["GET"])
@login_required
def stats_view():
    categories = Statistics.time_spent_on_category(current_user.id)
    overall_time = datetime.timedelta(0)
    for i in categories.keys():
        overall_time += categories[i][1]

    return render_template(
        "statistics/stats_view.html",
        categories=categories,
        category_ids=categories.keys(),
        events=list(Event.find_events_user_has_permissions_to(current_user.id)),
        overall_time=overall_time,
        user=current_user,
        form=CategoryForm,
        str=str
    )
