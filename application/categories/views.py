from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm

from application.events.models import Event
from application.clips.models import Clip


@app.route("/categories", methods=["GET", "POST"])
@login_required
def categories_index():
    return render_template(
        "categories/list.html",
        categories=list(Category.query.filter(Category.account_id == current_user.id)),
        form=CategoryForm(),
        delete_error=""
    )


@app.route("/categories/new")
@login_required
def categories_form():
    return render_template("categories/new.html", form=CategoryForm())


@app.route("/categories/<category_id>/edit", methods=["POST"])
@login_required
def categories_edit(category_id):
    if Category.query.filter_by(id=category_id).first().account_id == current_user.id:
        form = CategoryForm(request.form)

        if not form.validate():
            form.description.data, form.description.data = "", ""
            return render_template(
                "categories/list.html",
                categories=list(Category.query.filter(Category.account_id == current_user.id)),
                form=form
            )

        c = Category.query.get(category_id)

        c.name = form.name.data
        c.description = form.description.data
        db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/<category_id>/delete", methods=["POST"])
@login_required
def categories_delete(category_id):
    if Category.query.filter_by(id=category_id).first().account_id == current_user.id:
        if not Event.query.filter_by(category_id=category_id) or not Category.query.join(Clip.categories).filter(Category.id == category_id).all():
            c = Category.query.get(category_id)

            db.session.delete(c)
            db.session().commit()
        else:
            return render_template(
                "categories/list.html",
                categories=list(Category.query.filter(Category.account_id == current_user.id)),
                form=CategoryForm(),
                delete_error="This category can't be deleted as it has Events or Clips associated with it."
            )

    return redirect(url_for("categories_index"))


@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form=form)

    if Category.query.filter(Category.account_id == current_user.id).filter(Category.name == form.name.data).first():
        form.name.errors.append("Category named " + form.name.data + " already exists.")
        return render_template("categories/new.html", form=form)

    c = Category(form.name.data, form.description.data)
    c.account_id = current_user.id

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))
