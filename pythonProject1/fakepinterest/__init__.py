# importa nosso flask, cria nossa aplicação

# render_template busca a pasta templates
#url for - mudar a url para o nome da função
from flask import Flask

# criação do site -- Começar por aqui
app = Flask(__name__)


# importacoes de outros arquivos no init são aqui no final  
from fakepinterest import routes