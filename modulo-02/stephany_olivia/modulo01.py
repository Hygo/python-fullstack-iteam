# Atividades de Python - Módulo 01

#Exercício 01----------------------------------
print("Olá, Mundo!")

nome = "Stephany Olivia da Silva Pereira"
print(nome)

print("Python: simples, poderoso e elegante.")

#Exercício 02-----------------------------------
import sys

print(f"Versão do Python instalada: {sys.version}")

print(f"Sistema operacional em uso: {sys.platform}")

#Exercício 03-------------------------------------
import this

# REFLEXÃO SOBRE O ZEN OF PYTHON:
# O princípio que mais faz sentido para mim é "Explicit is better than implicit" 
# (O explícito é melhor do que o implícito). Na programação, tentar ser "esperto" 
# demais e esconder lógica atrás de truques mágicos ou códigos super compactos 
# sempre cobra o seu preço no futuro. É muito melhor escrever um código claro, 
# onde qualquer pessoa que leia entenda exatamente o que está acontecendo, 
# do que um código curto que parece feitiçaria, mas ninguém consegue dar manutenção depois.

#Exercício 04--------------------------------------
"""
Módulo de Exemplo: Cadastro de Funcionário.

Este script demonstra a declaração de variáveis de diferentes tipos primitivos
(String, Inteiro, Float e Booleano) no Python e a exibição simplificada 
desses dados no console.
"""

# Armazena o nome completo do funcionário (tipo: str - String/Texto)
nome = "Ana Lima"

# Armazena a idade do funcionário em anos (tipo: int - Inteiro)
idade = 29

# Armazena o salário mensal em reais (tipo: float - Número de ponto flutuante)
salario = 4500.00

# Armazena o status de cadastro, indicando se está ativo (tipo: bool - Booleano)
ativo = True

# Exibe todos os valores das variáveis na tela, separados por um espaço em branco
print(nome, idade, salario, ativo)

#Exercício 05--------------------------------------
# print estava com o P maiúsculo, o que causava um erro de sintaxe. Corrigido para "print" com p minúsculo.
print("Bem-vindo ao curso de Python") 

# Carlos estava sem aspas no final 
nome = "Carlos"

print("Aluno: " + nome)

# O texto "Curso de Python" estava sem aspas.
print("Curso de Python")

#Exercício 06--------------------------------------

ano_atual = 2026
temperatura = 27.5
cidade = "Boa Vista"
esta_chovendo = False
previsao = None
texto_vazio = ""

print(f"Valor: {ano_atual} | Tipo: {type(ano_atual)}")
print(f"Valor: {temperatura} | Tipo: {type(temperatura)}")
print(f"Valor: '{cidade}' | Tipo: {type(cidade)}")
print(f"Valor: {esta_chovendo} | Tipo: {type(esta_chovendo)}")
print(f"Valor: {previsao} | Tipo: {type(previsao)}")
print(f"Valor: '{texto_vazio}' | Tipo: {type(texto_vazio)}")

#Exercício 07--------------------------------------
largura = 12.5
comprimento = 30.0

area = largura * comprimento
print(f"A área do terreno é: {area:.1f} m²")

#Exercício 08--------------------------------------
celsius = 36.5

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# Exibição dos resultados formatados
print("--- Conversor de Temperatura ---")
print(f"Celsius:    {celsius:.1f} °C")
print(f"Fahrenheit: {fahrenheit:.1f} °F")
print(f"Kelvin:     {kelvin:.2f} K")

#Exercício 09--------------------------------------
# Solicitando os dados do usuário
nome = input("Digite o seu nome: ")
idade_str = input("Digite a sua idade: ")

# Convertendo a idade de texto (string) para número inteiro (int)
idade = int(idade_str)

# Calculando o ano aproximado de nascimento (considerando o ano atual como 2026)
ano_atual = 2026
ano_nascimento = ano_atual - idade

# Exibindo a mensagem personalizada
print(f"Olá, {nome}! Você tem {idade} anos e nasceu por volta de {ano_nascimento}.")

#Exercício 10--------------------------------------
# Dados do problema
capacidade_caminhao = 850
peso_caixa = 32

# Calculando a quantidade de caixas completas (Divisão Inteira)
caixas_completas = capacidade_caminhao // peso_caixa

# Calculando o peso que sobra (Resto da Divisão)
peso_restante = capacidade_caminhao % peso_caixa

# Exibindo os resultados
print(f"O caminhão pode carregar {caixas_completas} caixas completas.")
print(f"Ficarão sobrando {peso_restante} kg de capacidade que não completam uma caixa.")


