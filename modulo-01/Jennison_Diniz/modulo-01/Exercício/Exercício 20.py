# Solicitar dados ao usuário
capital_inicial = float(input("Digite o capital inicial (R$): "))
taxa_juros = float(input("Digite a taxa de juros ao mês (%): ")) / 100
periodo = int(input("Digite o período em meses: "))

# Cálculo do montante
montante = capital_inicial * (1 + taxa_juros * periodo)

# Juros totais
juros_totais = montante - capital_inicial

# Exibição formatada
print("\n--- Resultado da Simulação ---")
print(f"Capital inicial: R$ {capital_inicial:,.2f}")
print(f"Taxa de juros ao mês: {taxa_juros*100:.2f}%")
print(f"Período: {periodo} meses")
print(f"Juros totais: R$ {juros_totais:,.2f}")
print(f"Montante final: R$ {montante:,.2f}")
