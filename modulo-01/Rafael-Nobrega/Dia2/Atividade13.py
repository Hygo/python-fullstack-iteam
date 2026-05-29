## 13 – Operadores Lógicos e de Comparação

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

print("1) O primeiro número é maior que o segundo?")
print( a > b)
print("2) Os dois são iguais?")
print( a == b)
print("3) Ambos são positivos?")
print( a > 0 and b > 0)
print("4) Pelo menos um é maior que 100?")
print( a > 100 or b > 100)
print("5) O primeiro é diferente de zero?")
print( a != 0)
