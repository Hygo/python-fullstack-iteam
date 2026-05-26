# 1. Solicitando a distância em metros
metros = float(input("Digite a distância em metros (m): "))

# 2. Realizando os cálculos de conversão
km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084

# 3. Exibindo o cabeçalho da tabela
print("\n" + "=" * 35)
print(f"CONVERSÃO DE: {metros:.2f} METROS")
print("-" * 35)
# O símbolo < alinha à esquerda e > alinha à direita. O número define a largura.
print(f"{'Unidade':<15} | {'Valor Convertido':>15}")
print("-" * 35)

# 4. Exibindo as linhas da tabela perfeitamente alinhadas
print(f"{'Quilômetros':<15} | {km:>15.4f} km")
print(f"{'Centímetros':<15} | {cm:>15.2f} cm")
print(f"{'Milímetros':<15} | {mm:>15.2f} mm")
print(f"{'Polegadas':<15} | {polegadas:>15.2f} in")
print(f"{'Pés':<15} | {pes:>15.2f} ft")
print("=" * 35)