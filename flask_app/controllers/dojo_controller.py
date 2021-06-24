from flask_app import app
from flask import render_template, request, session, redirect
from ..models.dojo import Dojo




@app.route("/")
def index():
    dojos = Dojo.get_all_dojos()

    return render_template("index.html", all_dojos = dojos)


@app.route("/create", methods = ["POST"])
def create_dojo():
    print(request.form)
    Dojo.create(request.form)

    return redirect("/")


@app.route("/<int:dojo_id>/dojo_ninjas")
def get_all_ninjas(dojo_id):
    dojos = Dojo.get_dojo({'id' : dojo_id})

    return render_template("/dojo_ninjas.html", dojo = dojos) 