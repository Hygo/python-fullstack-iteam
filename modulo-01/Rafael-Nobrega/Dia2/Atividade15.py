# 15 - Calculadora de Desconto 

compra = float(input("Digite o  valor da compra: "))

desconto = compra * (10/100)

compraFinal = compra - desconto

print(f"O valor da sua compra após o desconto de {desconto:.2f} é R$ {compraFinal:.2f}")