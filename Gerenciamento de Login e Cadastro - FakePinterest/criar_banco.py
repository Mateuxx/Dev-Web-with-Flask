from fakepinterest import database, app

# importas as duas classes(colunas do db ) para criar o banco de dados corretamente.
from fakepinterest.models import Usuario, Foto

# criaçao do banco de dados
with app.app_context():
    database.create_all()
