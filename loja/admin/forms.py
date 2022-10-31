from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('nome', [validators.Length(min=4, max=25)])
    usuario = StringField('usuario', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=35)])
    senha = PasswordField('senha, [
        validators.DataRequired(),
        validators.EqualTo('confirmar senha', message='senhas diferentes')
    ])
    confirm = PasswordField('repita sua senha')