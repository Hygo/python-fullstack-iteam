## 12 – Calculadora de IMC

peso = float(input("Digite o seu Peso?"))
altura = float(input("Digite a sua Altura?"))
imc = (peso / (altura * altura))

print(f"Você tem {peso} kgs")
print(f"Você tem {altura} m")
print(f"o seu é IMC é {imc:.2f}")