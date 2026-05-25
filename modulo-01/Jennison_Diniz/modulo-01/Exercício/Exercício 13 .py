# Solicitando e armazenando os dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n" + "="*40)
print("         RESULTADOS LÓGICOS")
print("="*40)

# 1. O primeiro número é maior que o segundo?
print(f"O primeiro é maior que o segundo? {num1 > num2}")

# 2. Os dois são iguais?
print(f"Os dois são iguais? {num1 == num2}")

# 3. Ambos são maiores que zero? (Operador AND)
print(f"Ambos são maiores que zero? {num1 > 0 and num2 > 0}")

# 4. Pelo menos um é maior que 100? (Operador OR)
print(f"Pelo menos um é maior que 100? {num1 > 100 or num2 > 100}")

# 5. O primeiro é diferente de zero? (Operador de diferença)
print(f"O primeiro é diferente de zero? {num1 != 0}")

print("="*40)