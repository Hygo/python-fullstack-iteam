### 🟢 Exercício 09 – Boas-vindas Personalizada
# Escreva um script que:
# 1. Solicite ao usuário seu **nome** (`input()`)
# 2. Solicite sua **idade**
# 3. Exiba: `Olá, [nome]! Você tem [idade] anos e nasceu por volta de [ano_nascimento].`
# > 💡 *`input()` sempre retorna string. Para cálculos, converta com `int()`.*

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

aniversario = input("Você já fez aniversário este ano? (s/n): ").strip().lower()

ano_atual = 2026
ano_nascimento = ano_atual - idade

if aniversario == "n":
    ano_nascimento -= 1

print(f"Olá, {nome}! Você tem {idade} anos e nasceu em {ano_nascimento}.")