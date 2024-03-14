# importa nosso flask, cria nossa aplicação

# render_template busca a pasta templates
#url for - mudar a url para o nome da função
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# criação do site -- Começar por aqui
app = Flask(__name__)

# criacao do bando de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

database = SQLAlchemy(app)

# importacoes de outros arquivos no init são aqui no final  
from fakepinterest import routes