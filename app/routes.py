from app import app
from flask import render_template
from app import forms


@app.route('/', methods=['POST', 'GET'])
def sign_in():  # put application's code here
    form = forms.LoginForms()
    return render_template('index.html', form=form)


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print(form.data)
    return render_template('registration.html', form=form)
