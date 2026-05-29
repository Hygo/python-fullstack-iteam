### 🟡 Exercício 15 – Calculadora de Desconto
# Uma loja aplica 10% de desconto em todas as compras.
# Peça o valor da compra, calcule o desconto e valor final, exibindo tudo formatado em reais.

valor = float(input("Digite o valor da compra: R$ "))

desconto = valor * 0.10
valor_final = valor - desconto

def brl(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print(f"\nValor original : R$ {brl(valor)}")
print(f"Desconto (10%) : R$ {brl(desconto)}")
print(f"Valor final    : R$ {brl(valor_final)}")
