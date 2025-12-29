print("** SISTEMA DE LOGIN **")

#constantes
USER_VALIDO = "adm"
PASSWORD_VALIDO = "123"

#inputs
user = input("Digite o usuario: ")
password = input("Digite a sua senha: ")

#definindo saida
if user == USER_VALIDO and password == PASSWORD_VALIDO:
    print("Bem-vindo ao sistema")
elif user == USER_VALIDO:
    print("Senha incorreta")
elif password == PASSWORD_VALIDO:
    print("Usuario incorreto")
else:
    print("Usuario e senha invalidos")