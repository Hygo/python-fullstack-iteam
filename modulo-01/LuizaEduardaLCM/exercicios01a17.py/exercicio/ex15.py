import this

valorCompra = input("Digite o valor da compra: ")
valorDesconto = float(valorCompra) * 0.15
valorFinal = float(valorCompra) - valorDesconto
print("Valor da compra: R$", valorCompra)
print("Valor do desconto: R$", valorDesconto)
print("Valor a pagar: R$", valorFinal)