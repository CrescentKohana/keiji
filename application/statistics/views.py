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
    categories = list(Category.query.filter(Category.account_id == current_user.id))
    return render_template(
        "statistics/stats_view.html",
        categories=categories,
        category_time=Statistics.time_spent_on_category(current_user.id),
        categories_len=len(categories),
        events=list(Event.find_events_user_has_permissions_to(current_user.id)),
        user=current_user,
        form=CategoryForm
    )
