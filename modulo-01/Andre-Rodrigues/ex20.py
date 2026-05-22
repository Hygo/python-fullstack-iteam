capital = float(input("Capital inicial (R$): "))
taxa = float(input("Taxa de juros ao mês (%): "))
periodo = int(input("Período (meses): "))

taxa_decimal = taxa / 100 #Converter porcentagem para decimal
montante = capital * (1 + taxa_decimal * periodo) 
juros_totais = montante - capital


print("\n=== RESUMO DO INVESTIMENTO ===")
print(f"Capital Inicial: R$ {capital:.2f}")
print(f"Taxa de Juros  : {taxa}% ao mês")
print(f"Período        : {periodo} meses")
print(f"Juros Totais   : R$ {juros_totais:.2f}")
print(f"Montante Final : R$ {montante:.2f}")