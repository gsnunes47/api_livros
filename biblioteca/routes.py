from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from biblioteca import app, database
from biblioteca.models import Livros

@app.route('/livros', methods=['GET'])
def obter_livro():
    livros = []
    livros_query = Livros.query.all()
    for l in livros_query:
        l = l.__dict__
        treat = l.pop('_sa_instance_state')
        livros.append(l)
    return jsonify(livros)

@app.route('/livros', methods=['POST'])
def criar_novo_livro():
    livro_novo = request.get_json()
    livro = Livros(id=livro_novo['id'], autor=livro_novo['autor'], titulo=livro_novo['titulo'])
    database.session.add(livro)
    database.session.commit()
    livro_json = Livros.query.filter_by(titulo=livro_novo['titulo']).first().__dict__
    treat = livro_json.pop('_sa_instance_state')
    return jsonify(livro_json)

@app.route('/livros/<id>', methods=['GET'])
def obter_livro_por_id(id):
    livro = Livros.query.filter_by(id=id).first().__dict__
    treat = livro.pop('_sa_instance_state')
    return jsonify(livro)

@app.route('/livros/<id>', methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    livro = Livros.query.filter_by(id=id).first()
    livro.autor = livro_alterado['autor']
    livro.titulo = livro_alterado['titulo']
    database.session.commit()
    livro = Livros.query.filter_by(id=id).first().__dict__
    treat = livro.pop('_sa_instance_state')
    return jsonify(livro)


