from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.clips.models import Clip
from application.clips.forms import ClipForm

from application.categories.models import Category


@app.route("/clips", methods=["GET", "POST"])
@login_required
def clips_index():
    return render_template(
        "clips/list.html",
        clips=list(Clip.find_clips_user_has_permissions_to(current_user.id)),
        category=Category.query.filter(Category.id == Clip.category_id).first(),
        form=ClipForm()
    )


@app.route("/clips/new")
@login_required
def clips_form():
    return render_template("clips/new.html", form=ClipForm())


@app.route("/clips/<clip_id>/edit", methods=["POST"])
@login_required
def clips_edit(clip_id):
    if Clip.get_clip_owner(clip_id) == current_user.id:
        form = ClipForm(request.form)

        if not form.validate():
            form.content.data = ""
            return render_template(
                "clips/list.html",
                clips=list(Clip.find_clips_user_has_permissions_to(current_user.id)),
                category=Category.query.filter(Category.id == Clip.category_id).first(),
                form=form
            )

        c = Clip.query.get(clip_id)

        c.category_id = form.category_id.data.id
        c.content = form.content.data
        db.session().commit()

    return redirect(url_for("clips_index"))


@app.route("/clips/<clip_id>/delete", methods=["POST"])
@login_required
def clips_delete(clip_id):
    if Clip.get_clip_owner(clip_id) == current_user.id:
        c = Clip.query.get(clip_id)

        db.session.delete(c)
        db.session().commit()

    return redirect(url_for("clips_index"))


@app.route("/clips/", methods=["POST"])
@login_required
def clips_create():
    form = ClipForm(request.form)

    if not form.validate():
        return render_template("clips/new.html", form=form)

    c = Clip(request.form['category_id'], request.form['content'])

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("clips_index"))
