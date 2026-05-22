capital = float(input("Capital inicial: "))
taxa = float(input("Taxa de juros ao mês (%): "))
meses = int(input("Período em meses: "))

montante = capital * (1 + (taxa / 100) * meses)
juros_totais = montante - capital

print(f"\nCapital   : R$ {capital:.2f}")
print(f"Taxa      : {taxa:.2f}% ao mês")
print(f"Período   : {meses} meses")
print(f"Juros     : R$ {juros_totais:.2f}")
print(f"Montante  : R$ {montante:.2f}")
