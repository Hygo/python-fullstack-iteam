descricao = input("Descrição do produto: ")
quantidade = int(input("Quantidade: "))
preco_unit = float(input("Preço unitário: R$ "))

subtotal = quantidade * preco_unit
imposto = subtotal * 0.12
total = subtotal + imposto

print("\n===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: R$ {preco_unit:.2f}")
print(f"Subtotal  : R$ {subtotal:.2f}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : R$ {total:.2f}")
print("=======================")
