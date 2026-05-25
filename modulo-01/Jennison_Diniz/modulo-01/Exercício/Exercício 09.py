# Solicitando o nome do usuário
nome = input("Digite o seu nome: ")

# Solicitando a idade e convertendo para número inteiro (int)
idade = int(input("Digite a sua idade: "))

# Calculando o ano de nascimento aproximado baseado no ano atual (2026)
ano_nascimento = 2026 - idade

# Exibindo a mensagem personalizada
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")