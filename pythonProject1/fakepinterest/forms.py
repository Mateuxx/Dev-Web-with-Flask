# formularios do nosso site 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario
from fakepinterest.forms import FormLogin, FormCriarConta

class FormLogin(FlaskForm):
    email =  StringField("E-mail", validators=[DataRequired(), Email()])
    senha =  PasswordField("Senha", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mal", validators= [DataRequired(), Email()])
    username= StringField("Nome de usuario", validators=[DataRequired()] )
    senha = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao =  SubmitField("Criar conta")
    
    def validate_email(self, email):
        # Vendo se ja existe esse email em nosso Banco De dados
        # email.data para pegar as informações que tem nele
        usuario = Usuario.query.filter_by(email=email.data).first()
        
        # se usuario tiver alguma coisa retorno esssa exeception abaixo:
        if usuario:
            return ValidationError("E-mail ja cadastrado, faça login para continuar")