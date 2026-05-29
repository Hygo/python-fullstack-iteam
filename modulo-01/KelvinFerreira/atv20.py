### 🔴 Exercício 20 – Calculadora de Investimento Simples
# Solicite: capital inicial, taxa de juros ao mês (%) e período em meses.
# Fórmula: M = C × (1 + i × t)
# Exiba capital, taxa, período, juros totais e montante final formatados.

capital = float(input("Capital inicial (R$): "))
taxa = float(input("Taxa de juros ao mês (%): "))
periodo = int(input("Período (meses): "))

montante = capital * (1 + (taxa / 100) * periodo)
juros = montante - capital

def brl(v):
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

print("\n===== RESUMO DO INVESTIMENTO =====")
print(f"Capital inicial : R$ {brl(capital)}")
print(f"Taxa de juros   : {taxa:.2f}% ao mês")
print(f"Período         : {periodo} mês(es)")
print(f"Juros totais    : R$ {brl(juros)}")
print(f"Montante final  : R$ {brl(montante)}")
print("==================================")
