print("=== Método 1: com variável auxiliar ===")
a = 10
b = 20
aux = a   # guarda o valor original de 'a'
a = b     # 'a' recebe o valor de 'b'
b = aux   # 'b' recebe o valor original de 'a'
print(a, b)  # Esperado: 20 10

print("=== Método 2: idiomático do Python (tuple unpacking) ===")
a = 10
b = 20
a, b = b, a   # Python avalia o lado direito antes de atribuir
print(a, b)  # Esperado: 20 10
