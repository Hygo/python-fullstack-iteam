capital = float(input("Capital inicial (R$): "))
taxa = float(input("Taxa de juros ao mês (%): "))
periodo = int(input("Período (meses): "))

i = taxa / 100
montante = capital * (1 + i * periodo)
juros_totais = montante - capital

print(f"\nCapital inicial : R$ {capital:.2f}")
print(f"Taxa mensal     : {taxa:.2f}%")
print(f"Período         : {periodo} mês(es)")
print(f"Juros totais    : R$ {juros_totais:.2f}")
print(f"Montante final  : R$ {montante:.2f}")
