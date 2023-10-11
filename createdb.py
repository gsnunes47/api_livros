from biblioteca import database, app
from biblioteca.models import Livros

with app.app_context():
    database.create_all()
