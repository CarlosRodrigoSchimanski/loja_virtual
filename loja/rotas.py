from flask import render_template, session, request, url_for
from loja import app, db

@app.route('/')
def index():
    return 'seja bem vindo'