from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.events.models import Event
from application.events.forms import EventForm

from application.categories.models import Category


@app.route("/events", methods=["GET", "POST"])
@login_required
def events_index():
    return render_template(
        "events/list.html",
        events=list(Event.find_events_user_has_permissions_to(current_user.id)),
        category=Category.query.filter(Category.id == Event.category_id).first(),
        form=EventForm()
    )


@app.route("/events/new")
@login_required
def events_form():
    return render_template("events/new.html", form=EventForm())


@app.route("/events/<event_id>/edit", methods=["POST", "GET"])
@login_required
def events_edit(event_id):
    if request.method == "GET":
        events_index()

    if Event.get_event_owner(event_id) == current_user.id:
        form = EventForm(request.form)

        if not form.validate():
            form.description.data, form.duration.data = "", 0
            return render_template(
                "events/list.html",
                events=list(Event.find_events_user_has_permissions_to(current_user.id)),
                category=Category.query.filter(Category.id == Event.category_id).first(),
                form=form
            )

        c = Event.query.get(event_id)

        c.category_id = form.category_id.data.id
        c.description = form.description.data
        c.duration = form.duration.data
        db.session().commit()

    return redirect(url_for("events_index"))


@app.route("/events/<event_id>/delete", methods=["POST", "GET"])
@login_required
def events_delete(event_id):
    if request.method == "GET":
        events_index()

    if Event.get_event_owner(event_id) == current_user.id:
        c = Event.query.get(event_id)

        db.session.delete(c)
        db.session().commit()

    return redirect(url_for("events_index"))


@app.route("/events/", methods=["POST"])
@login_required
def events_create():
    form = EventForm(request.form)

    if not form.validate():
        return render_template("events/new.html", form=form)

    c = Event(request.form['category_id'], request.form['duration'], request.form['description'])

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("events_index"))
