# 17 - Análise de Nota Fiscal

desc = str(input("Poderia digitar o nome do produto: "))
quant = int(input("poderia digitar a quantidade desse produto: "))
precoUnit = float(input("Poderia digitar o preço unitario desse produto: "))
subtotal = quant * precoUnit
imposto = (subtotal * (12/100))
total = subtotal + imposto

print("===== NOTA FISCAL =====")
print(f"Produto   : {desc}")
print(f"Quantidade: {quant} unidade(s)")
print(f"Preço Unit: R$ {precoUnit:.2f}")
print(f"Subtotal  : R$ {subtotal}")
print(f"Imposto   : R$ {imposto:.2f}")
print(f"Total     : R$ {total:.2f}")
print("=======================")