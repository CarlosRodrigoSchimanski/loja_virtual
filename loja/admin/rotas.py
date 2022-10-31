from turtle import title
from flask import render_template, session, request, url_for, flash
from loja import app, db
from .forms import RegistrationForm

@app.route('/')
def homee():
    return 'seja bem vindo a qui'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        #user = User(form.username.data, form.email.data,
                    #form.password.data)
        #db_session.add(user)
        flash('obrigado por registrar')
        return redirect(url_for('login'))
    return render_template('registrar.html', form=form, title='pagina de registro')