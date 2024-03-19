# importa nosso flask, cria nossa aplicação

# render_template busca a pasta templates
#url for - mudar a url para o nome da função
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#para o login e senha 
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# criação do site -- Começar por aqui
app = Flask(__name__)

# criacao do bando de dados
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"

# secret key - chave de segurança na qual eh requerida 
# feita no console do python por 
# import secrets
# print(secrets.token_hex(16))
app.config["SECRET_KEY"] = "d6f9d4d884a3c694cc8c5f49a481762b"

database = SQLAlchemy(app)

#gerenciamento para o login e senha 
bcrpyt = Bcrypt(app)
login_manager = LoginManager(app)

# qual o nome da view/routes que vai receber esse login - a tela que vais colocar o login, basicamente
# pode se escolher outra view/route para receber esse login.
login_manager.login_view = "homepage"


# importacoes de outros arquivos no init são aqui no final  
from fakepinterest import routes