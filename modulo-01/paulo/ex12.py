peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

print(f"O seu IMC é de {imc:.2f}.")
