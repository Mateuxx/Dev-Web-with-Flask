# render_template busca a pasta templates
#url for - mudar a url para o nome da função
from flask import Flask, render_template, url_for

# criação do site -- Começar por aqui
app = Flask(__name__)


# caminho do link do site - criação da rota o que aparece depois do dominio principal
@app.route("/")
def homepage():
    return render_template("homepage.html")

# <usuario> - isso significa uma variavel, na qual podemos usar o python dentro do html/css
@app.route("/perfil/<user>")
def perfil(user):
    return render_template("perfil.html", user=user)


# simular servidor local, garantindo a sergurança para quandoe ele for implementado
if __name__ == "__main__":
    app.run(debug=True)
