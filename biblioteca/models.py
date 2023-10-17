from biblioteca import database

class Livros(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    autor = database.Column(database.String, nullable=False)
