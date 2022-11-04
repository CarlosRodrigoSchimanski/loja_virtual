from flask import render_template, session, request, url_for, flash
from loja import app, db, bcrypt
from .forms import RegistrationForm
from .models import User
import os

@app.route('/')
def homee():
    return 'seja bem vindo a qui'


@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate(form.senha.data):
        hash_password = bcrypt.generate_password_hash()
        user = User(name=form.nome.data, username=form.usuario.data, email=form.email.data, password=hash_password)
        db.session.add(user)
        flash('obrigado por registrar')
        return redirect(url_for('login'))
    return render_template('admin/registrar.html', form=form, title='pagina de registro')