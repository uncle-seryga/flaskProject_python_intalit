import db_controller
import gamerules
from app import app
from flask import render_template, render_template_string, flash
from app import forms


@app.route('/', methods=['POST', 'GET'])
def sign_in():  # put application's code here
    form = forms.LoginForms()
    if form.validate_on_submit():
        login = form.login.data
        print(login)
        data = db_controller.Users().get(login)
        if not data:
            print(data)
            flash("No such user!")
            # return render_template_string('No such user!')
        else:
            print("Success")
            if form.password.data == data[0][2]:
                return render_template('gamefield.html', form=forms.Gamefield(), word=gamerules.set_mask(gamerules.get_word()))
            else:
                flash("Wrong password")
    return render_template('index.html', form=form)


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template('registration.html', form=form)
