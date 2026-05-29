peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print(f"\nIMC calculado: {imc:.2f}")
print("Classificação:", end=" ")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
elif imc < 35:
    print("Obesidade Grau I")
elif imc < 40:
    print("Obesidade Grau II")
else:
    print("Obesidade Grau III")
