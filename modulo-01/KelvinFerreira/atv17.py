### 🔴 Exercício 17 – Análise de Nota Fiscal
# Solicite descrição do produto, quantidade e preço unitário via input().
# Exiba a nota fiscal formatada com subtotal, imposto (12%) e total.

descricao = input("Descrição do produto: ")
quantidade = int(input("Quantidade: "))
preco_unitario = float(input("Preço unitário: R$ "))

subtotal = quantidade * preco_unitario
imposto = subtotal * 0.12
total = subtotal + imposto

def brl(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print("\n===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: R$ {brl(preco_unitario)}")
print(f"Subtotal  : R$ {brl(subtotal)}")
print(f"Imposto   : R$ {brl(imposto)}")
print(f"Total     : R$ {brl(total)}")
print("=======================")
