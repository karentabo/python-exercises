#inputs from user
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
nome_empresa = input("Digite o nome da empresa: ")
dominio = input("Digite seu dominio (ex: com.br, com.mx, com.ar , etc: ")

#normalize data
nome = nome.strip().lower().replace(" ", ".")
sobrenome = sobrenome.strip().lower().replace(" ", ".")
nome_empresa = nome_empresa.strip().lower().replace(" ", "")
dominio = dominio.strip().lower().replace(" ", "")
email_gerado = f"{nome}.{sobrenome}@{nome_empresa}.{dominio}"

print(email_gerado)