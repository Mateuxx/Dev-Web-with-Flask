# lugar aonde vamos usar as routes do nosso site 
from flask import render_template, url_for

from fakepinterest import app

from flask_login import login_required

# caminho do link do site - criação da rota o que aparece depois do dominio principal
@app.route("/")
def homepage():
    return render_template("homepage.html")

# <usuario> - isso significa uma variavel, na qual podemos usar o python dentro do html/css
@app.route("/perfil/<user>")
# so pode ser acessada quando for feita o login 
@login_required
def perfil(user):
    return render_template("perfil.html", user=user)