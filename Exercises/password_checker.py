print('** PASSWORD CHECKER **')

password = input("Digite sua senha: ")

has_digit = False
has_upper = False

# Verifica cada caractere da senha
for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

# Verificação final
if len(password) >= 8 and has_digit and has_upper:
    print("Strong password!")
else:
    print("Weak password!")


