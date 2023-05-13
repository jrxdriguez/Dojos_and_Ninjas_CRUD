from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojos import Dojo

@app.route('/')
def display_dojos():
    
    all_dojos = Dojo.get_all_dojos()
    #print(all_dojos)
    return render_template('home.html',all_dojos = all_dojos) #add backin (): all_dojos = all_dojos

@app.route('/add_dojo', methods=['POST'])
def new_dojo():
    dojo_data = {
        'name' : request.form['name']
    }

    Dojo.add_dojo(request.form)
    return redirect('/')

@app.route('/new')
def ninja_form():

    all_dojos = Dojo.get_all_dojos()
    return render_template('ninja.html',all_dojos = all_dojos)

@app.route('/show_dojo/<int:id>')
def show_one_dojo(id):
    dojo_data = {'ID' : id}

    one_dojo = Dojo.get_one_dojo(dojo_data)
    return render_template('show_dojo.html', one_dojo = one_dojo)