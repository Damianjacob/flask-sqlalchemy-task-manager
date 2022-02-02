from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task



@app.route("/")
def home():
    return render_template("tasks.html")



@app.route("/categories")
def categories():
    return render_template("categories.html")


# We need POST for sending form data to the database and GET
# to access data of the database and display it to the user
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method =="POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")