descricao = input("Informe a descrição do novo produto:\n")
quantidade = int(input("Informe a quatidade do produto:\n"))
preco = float(input("Informe o preço unitário do novo produto:\n"))

print(f"""
===== NOTA FISCAL =====
Produto   : [{descricao}]
Quantidade: [{quantidade}] unidade(s)
Preço Unit: R$ [{preco}]
Subtotal  : R$ [{quantidade * preco}]
Imposto   : R$ [{(quantidade * preco) * 0.12}]
Total     : R$ [{(quantidade * preco) + ((quantidade * preco) * 0.12)}
=======================
""")