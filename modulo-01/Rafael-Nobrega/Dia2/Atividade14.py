## 14 – Troca de Variáveis

# 1 - Variável Auxiliar
a = 10
b = 20

aux = a
a = b
b = aux

print(a, b)  # Esperado: 20 10 — mas imprime 20 20

# 2 - Método Idiomático 

a = 10
b = 20

a,b = b,a 

print(a,b)