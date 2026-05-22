# Forma 1: Com variável auxiliar
a = 10
b = 20

aux = a
a = b
b = aux
print("Forma 1:", a, b)

# Forma 2: Método idiomático do Python (desempacotamento)
a = 10
b = 20

a, b = b, a
print("Forma 2:", a, b)
