import datetime

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

ano_atual = datetime.datetime.now().year
ano_nascimento = ano_atual - idade

print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")
