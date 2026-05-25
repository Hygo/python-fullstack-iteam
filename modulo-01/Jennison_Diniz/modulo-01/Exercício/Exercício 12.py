# Solicitando os dados do usuário
peso = float(input("Digite seu peso em kg (ex: 70.5): "))
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

# Calculando o IMC
# O operador ** é usado para elevar ao quadrado (altura²)
imc = peso / (altura ** 2)

# Exibindo o resultado formatado com 2 casas decimais
print("-" * 40)
print(f"Seu IMC atual é: {imc:.2f}")
print("-" * 40)

# Uma breve mensagem informativa baseada na tabela da OMS
if imc < 18.5:
    print("Classificação: Abaixo do peso ideal.")
elif imc < 25.0:
    print("Classificação: Peso normal (Parabéns!).")
elif imc < 30.0:
    print("Classificacão: Sobrepeso.")
else:
    print("Classificação: Obesidade.")