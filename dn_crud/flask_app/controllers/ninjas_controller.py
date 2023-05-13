from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.ninjas import Ninja


@app.route('/add_ninja', methods=['POST'])
def new_ninja():
    print(request.form['dojo_ID'])
    new_ninja_data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'age' : request.form['age'],
        'dojo_ID' : request.form['dojo_ID']
    }
    Ninja.add_ninja(new_ninja_data)
    return redirect('/')