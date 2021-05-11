from app import db


class Aluno(db.Model):
    ra = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(60))
    email = db.Column(db.String(50))
    logradouro = db.Column(db.String(50))
    numero = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    complemento = db.Column(db.String(60))

    def __init__(self, nome, email, logradouro, numero, cep, complemento):
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
