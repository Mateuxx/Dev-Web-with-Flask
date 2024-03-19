# FLASK - FORMS, LOGIN E CADASTRO:

### Forms no HTML:

<body>
    <h1>
        FakePinterest - meu primeiro site no ar
    </h1>

    <p>
       agora vamos sei la qualquer coisa manos
    </p>

    <form method="POST">
        
    </form>

</body>

### POST AND GET:

Ao entrar em sites ou navegar pela temos a seguinte **_questão_**:

- POST: Fazer a postagem, ou seja, seu servidor/sistema está **enviando** coisas para a a web
- GET: Seu sistema/servidor está **recebendo** algo do user.

### Implementando na tela de login:

<form method="POST">
    {{ form.csrf_token }}

    {{ form.email.label() }}
    {{ form.email() }}

    {{ form.senha.label() }}
    {{ form.senha() }}

    {{ form.botao_confirmacao() }}

</form>