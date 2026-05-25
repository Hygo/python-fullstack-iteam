from datetime import date

ano_atual = date.today().year

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
ano_nascimento = ano_atual - idade
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")