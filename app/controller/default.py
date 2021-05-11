from flask.helpers import flash
from app import app, db
from app.models.tables import Aluno
from app.models.utils import busca_logradouro
from flask import Flask, redirect, render_template, request, url_for
from flask_fontawesome import FontAwesome
from flask_sqlalchemy import SQLAlchemy


fa = FontAwesome(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list")
def list_all():
    alunos = Aluno.query.all()
    return render_template("list_all_students.html", alunos=alunos)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        logradouro = busca_logradouro(request.form['cep'])
        aluno = Aluno(request.form['nome'], request.form['email'],
                      logradouro, request.form['numero'], request.form['cep'],
                      request.form['complemento'])

        db.session.add(aluno)
        db.session.commit()

        return redirect(url_for('list_all'))
    return render_template('add_new_student.html')


@app.route("/edit/<int:ra>", methods=['GET', 'POST'])
def edit_student(ra):
    aluno = Aluno.query.get(ra)
    if request.method == 'POST':
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.cep = request.form['cep']
        aluno.numero = request.form['numero']
        aluno.complemento = request.form['complemento']
        aluno.logradouro = busca_logradouro(aluno.cep)
        db.session.commit()
        return redirect(url_for('list_all'))
    return render_template('edit_student.html', aluno=aluno)


@app.route("/delete/<int:ra>")
def delete(ra):
    aluno = Aluno.query.get(ra)
    db.session.delete(aluno)
    db.session.commit()
    return redirect(url_for('list_all'))
