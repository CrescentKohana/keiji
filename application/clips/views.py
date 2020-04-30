from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.clips.models import Clip
from application.clips.forms import ClipForm

from application.categories.models import Category


@app.route("/clips", methods=["GET", "POST"])
@login_required
def clips_index():
    clip_categories, trimmed_clips = transform_clips(list(Clip.find_clips_user_has_permissions_to(current_user.id)))

    return render_template(
        "clips/list.html",
        clips=trimmed_clips,
        clip_categories=clip_categories,
        category=Category.query.filter(Category.id == Clip.categories).first(),
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
            clip_categories, trimmed_clips = transform_clips(
                list(Clip.find_clips_user_has_permissions_to(current_user.id))
            )
            return render_template(
                "clips/list.html",
                clips=trimmed_clips,
                clip_categories=clip_categories,
                category=Category.query.filter(Category.id == Clip.categories).first(),
                form=form
            )

        c = Clip.query.get(clip_id)

        c.categories = form.category_id.data
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

    c = Clip(form.category_id.data, request.form['content'])

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("clips_index"))


def transform_clips(clips):
    clip_categories = {}

    # Transforms all categories with same clip to one string like this: "cat1, cat2, cat3"
    for clip in clips:
        for cat in Category.query.filter(Category.id == Clip.categories).first().query.filter_by(id=clip.category_id):
            if clip.id in clip_categories:
                clip_categories[clip.id] = clip_categories[clip.id] + "; " + cat.name
            else:
                clip_categories[clip.id] = cat.name

    # Trims all duplicated clips as categories with same clip are shown in one row.
    seen = set()
    trimmed_clips = []
    for clip in clips:
        if clip.id not in seen:
            seen.add(clip.id)
            trimmed_clips.append(clip)

    return clip_categories, trimmed_clips
