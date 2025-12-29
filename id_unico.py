from random import randint

#inputs
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
ano = input("Digite seu ano de nascimento (YYYY): ")

#normalize data
nome_2 = nome.strip().upper()[0:2]
sobrenome_2 = sobrenome.strip().upper()[0:2]
ano_2 = ano.strip()[-2:]

#generating ramdon numbers
num_aleatorio = randint(1000,9999)
id_unico = f"{nome_2}{sobrenome_2}{ano_2}{num_aleatorio}"

#printing data
print("** SISTEMA GERADOR DE ID UNICO **")

texto = f"""
Ola {nome.capitalize()}!
    Segue o ID gerado pelo sistema:
    {id_unico}
    Parabens!
"""
print(texto)




