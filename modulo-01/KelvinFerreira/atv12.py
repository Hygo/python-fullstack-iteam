### 🟡 Exercício 12 – Calculadora de IMC
# Fórmula: IMC = peso / altura²
# Solicite peso (kg) e altura (m) via input(), calcule o IMC
# e exiba com 2 casas decimais e mensagem informativa.

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / altura ** 2

print(f"\nIMC calculado: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25.0:
    classificacao = "Peso normal"
elif imc < 30.0:
    classificacao = "Sobrepeso"
elif imc < 35.0:
    classificacao = "Obesidade grau I"
elif imc < 40.0:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III (mórbida)"

print(f"Classificação : {classificacao}")
