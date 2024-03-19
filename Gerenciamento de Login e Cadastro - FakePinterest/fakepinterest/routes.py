# lugar aonde vamos usar as routes do nosso site 
from flask import render_template, url_for

from fakepinterest import app

from flask_login import login_required

from fakepinterest.forms import FormLogin, FormCriarConta


# caminho do link do site - criação da rota o que aparece depois do dominio principal
@app.route("/", methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    return render_template("homepage.html", form=formLogin)


# criação da página para o user criar a conta
@app.route("/criarconta", methods=["GET", "POST"])
def criarConta():
    formCriarConta = FormCriarConta()
    return render_template("criarConta.html", form=formCriarConta)


# <usuario> - isso significa uma variavel, na qual podemos usar o python dentro do html/css
@app.route("/perfil/<user>")
# so pode ser acessada quando for feita o login 
@login_required
def perfil(user):
    return render_template("perfil.html", user=user)
