# Variável auxiliar
a = 10
b = 20
x = a
a = b
b = x
print("Resultado Primeira Forma :", a, b)

# Método Pythonic
a = 10
b = 20
a, b = b, a
print("Resultado Pythonic:", a, b)