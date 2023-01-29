import db_controller
from app import app
from flask import render_template,render_template_string
from app import forms


@app.route('/', methods=['POST', 'GET'])
def sign_in():  # put application's code here
    form = forms.LoginForms()
    if form.validate_on_submit():
        data = db_controller.Users().get(form.login.data)
        if not data:
            return render_template_string('No such user!')
        else:
            if form.login.data == data[0][1]:
                return render_template_string('Welcome to the club, buddy')
            else:
                return render_template_string('Wrong password!')
    return render_template('index.html', form=form)


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template('registration.html', form=form)
