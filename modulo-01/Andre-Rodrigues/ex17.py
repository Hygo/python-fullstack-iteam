produto = input("Descrição do produto: ")
qtd = int(input("Quantidade: "))
preco = float(input("Preço unitário: "))

subtotal = qtd * preco
imposto = subtotal * 0.12
total = subtotal + imposto

print("\n===== NOTA FISCAL =====")
print(f"Produto   : {produto}")
print(f"Quantidade: {qtd} unidade(s)")
print(f"Preço Unit: R$ {preco:.2f}")
print(f"Subtotal  : R$ {subtotal:.2f}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : R$ {total:.2f}")
print("=======================")