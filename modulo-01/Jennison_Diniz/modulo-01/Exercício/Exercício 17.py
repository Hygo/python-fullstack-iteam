# 1. Solicitando os dados da Nota Fiscal via input()
descricao = input("Descrição do produto: ")
quantidade = int(input("Quantidade comprada: "))
preco_unitario = float(input("Preço unitário (R$): "))

# 2. Realizando os cálculos matemáticos
subtotal = quantidade * preco_unitario
imposto = subtotal * 0.12
total = subtotal + imposto

# 3. Função rápida para formatar os números no padrão de moeda brasileiro (R$ X.XXX,XX)
def formatar_real(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# 4. Exibindo a Nota Fiscal perfeitamente formatada
print("\n===== NOTA FISCAL =====")
print(f"Produto   : {descricao}")
print(f"Quantidade: {quantidade} unidade(s)")
print(f"Preço Unit: {formatar_real(preco_unitario)}")
print(f"Subtotal  : {formatar_real(subtotal)}")
print(f"Imposto   : {formatar_real(imposto)} (12%)")
print(f"Total     : {formatar_real(total)}")
print("=======================")