#CONSTANTES
USER = "admin"
PASSWORD = "123"

#ENTRADA DE DADOS
print("**SISTEMA DE AUTENTICACAO**")
user_input = input("Digite o usuario: ")
password_input = input("Digite a senha: ")

#VERIFICAR SE AS CREDENCIAIS ESTAO CORRETAS
if user_input == USER and password_input == PASSWORD:
    print("Credenciais corretas!!")
else:
    print("Usuario ou senha incorretos!!")