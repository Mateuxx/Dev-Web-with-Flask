# criar a estrutura do banco de dados

from fakepinterest import database, login_manager
from datetime import datetime

# qual a classe que vai gerenciar a estrutura de logins
# No nosso caso eh a classe Usuario
from flask_login import UserMixin

# carregar o usuario pelo seu id fazendo uma query 
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))


# criando cada classe como tabela semelhante ao ROOM do android
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable = False)
    
    # cada usuario pode ter apenas um email vinculado a uma conta 
    email = database.Column(database.String, nullable = False, unique=True)
    senha = database.Column(database.String, nullable = False)
    
    # relaçao, não eh uma coluna uma seta da tabela de usuarios para a tabela de fotos
    fotos = database.relationship("Foto", backref="usuario", lazy=True)

class Foto(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    
    # a imagem eh um texto pq o eh local aonde a imgagem está no meu sistema(dentro da pasta static)
    imagem = database.Column(database.String, default="default.png")
    
    # usando a lib datatime pra pegar a data atual
    data_criação = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    
    # chave estrangeira
    # essa ordem importa, exemplo chave de posicao, data cujo tem nome, esses que ficam marcados o nomezinho
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)