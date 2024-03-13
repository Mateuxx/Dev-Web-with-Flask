# render_template busca a pasta templates
from flask import Flask, render_template

# criação do site -- Começar por aqui
app = Flask(__name__)


# caminho do link do site - criação da rota o que aparece depois do dominio principal
@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/perfil")
def perfil():
    return render_template("perfil.html")


# simular servidor local, garantindo a sergurança para quandoe ele for implementado
if __name__ == "__main__":
    app.run(debug=True)
