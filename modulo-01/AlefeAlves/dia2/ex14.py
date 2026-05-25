a = 10
b = 20
a = b
b = a
print(a, b)  # Esperado: 20 10 — mas imprime 20 20

a1 = 10
b1 = 20
c1 = a1
a1 = b1
b1 = c1
print(a1, b1)  # Esperado: 20 10 

a = 10
b = 20
a, b = b, a
print(a, b)  # Esperado: 20 10