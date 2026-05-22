valor_compra = float(input("Digite o valor da compra (R$): "))

desconto = valor_compra * 0.10
valor_final = valor_compra - desconto

print(f"Desconto de 10%: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
