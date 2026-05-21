# 1. Solicitando o valor da compra ao usuário
valor_compra = float(input("Digite o valor total da compra (R$): "))

# 2. Calculando o desconto (10%) e o valor final
valor_desconto = valor_compra * 0.10
valor_final = valor_compra - valor_desconto

# 3. Formatando os valores para o padrão de moeda brasileiro (R$ X.XXX,XX)
# Usamos a formatação de f-string e o .replace() para ajustar os pontos e vírgulas
compra_pt = f"R$ {valor_compra:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
desconto_pt = f"R$ {valor_desconto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
final_pt = f"R$ {valor_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# 4. Exibindo o cupom de desconto formatado na tela
print("\n" + "="*35)
print("       EXTRATO DA COMPRA")
print("="*35)
print(f"Valor Original : {compra_pt}")
print(f"Desconto (10%) : {desconto_pt}")
print("-" * 35)
print(f"Valor Final    : {final_pt}")
print("="*35)