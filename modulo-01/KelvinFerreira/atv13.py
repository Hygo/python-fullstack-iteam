### 🟡 Exercício 13 – Operadores Lógicos e de Comparação
# Sem usar `if`, armazene dois números e use print() para responder (True/False):
# 1. O primeiro número é maior que o segundo?
# 2. Os dois são iguais?
# 3. Ambos são positivos?
# 4. Pelo menos um é maior que 100?
# 5. O primeiro é diferente de zero?

a = 15
b = 8

print(f"Números: a = {a}, b = {b}")
print()
print(f"O primeiro é maior que o segundo? {a > b}")
print(f"Os dois são iguais?               {a == b}")
print(f"Ambos são positivos?              {a > 0 and b > 0}")
print(f"Pelo menos um é maior que 100?    {a > 100 or b > 100}")
print(f"O primeiro é diferente de zero?   {a != 0}")
