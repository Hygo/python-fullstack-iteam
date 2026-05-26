# Código Original do Exercício:
# a = 10
# b = 20
# a = b
# b = a
# print(a, b)  # Erro: imprime 20 20

print("======= FORMA 1: VARIÁVEL AUXILIAR =======")
a = 10
b = 20

# Correção usando o terceiro "copo" para guardar o valor
auxiliar = a
a = b
b = auxiliar

print(a, b)  # Resultado: 20 10


print("\n======= FORMA 2: MÉTODO IDIOMÁTICO (PYTHON) =======")
a = 10
b = 20

# Correção usando a atribuição múltipla nativa do Python
a, b = b, a

print(a, b)  # Resultado: 20 10