from flask_app import app
from flask import render_template, request, session, redirect
from flask_app.models.new_ninjas import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    dojos = Dojo.get_all_dojos()

    return render_template('new_ninja.html', dojos = dojos)

@app.route('/ninjas/post',methods=['POST'])
def new_ninja():
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'age':request.form['age'],
        'dojo_id':request.form['dojo_id']
    }
    Ninja.insert(data)
    dojo_number = request.form['dojo_options']
    return redirect(f'/dojos/{dojo_number}')