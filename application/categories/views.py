from flask import redirect, render_template, request, url_for
from application import app, db
from application.categories.models import Category
from application.categories.forms import CategoryForm


@app.route("/categories", methods=["GET"])
def categories_index():
    return render_template("categories/list.html", categories=Category.query.all())


@app.route("/categories/new/")
def categories_form():
    return render_template("categories/new.html", form=CategoryForm())


@app.route("/categories/<category_id>/", methods=["POST"])
def categories_edit(category_id):
    form = CategoryForm(request.form)
    c = Category.query.get(category_id)

    c.name = form.name.data
    c.description = form.description.data
    db.session().commit()

    return redirect(url_for("categories_index"))


@app.route("/categories/", methods=["POST"])
def categories_create():
    form = CategoryForm(request.form)

    if not form.validate():
        return render_template("categories/new.html", form=form)

    c = Category(form.name.data, form.description.data)

    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))
