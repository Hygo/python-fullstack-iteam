### 🟡 Exercício 14 – Troca de Variáveis
# Corrija o código abaixo de duas formas:
# com variável auxiliar e com o método idiomático do Python.
#
# Problema original (imprime 20 20 em vez de 20 10):
#   a = 10
#   b = 20
#   a = b   ← sobrescreve a antes de salvar o valor
#   b = a
#   print(a, b)

# --- Forma 1: variável auxiliar ---
a = 10
b = 20
aux = a
a = b
b = aux
print("Com variável auxiliar:", a, b)  # 20 10

# --- Forma 2: desempacotamento idiomático do Python ---
a = 10
b = 20
a, b = b, a
print("Com desempacotamento :", a, b)  # 20 10
