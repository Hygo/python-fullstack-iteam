### 🔴 Exercício 18 – Conversão de Unidades Encadeada
# Solicite uma distância em metros e converta para:
# km, cm, mm, polegadas e pés.
# Exiba em tabela formatada com alinhamento usando f-strings.

metros = float(input("Digite a distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084

print(f"\n{'Unidade':<14} {'Valor':>18}")
print("-" * 33)
print(f"{'Metros':<14} {metros:>18.4f}")
print(f"{'Quilômetros':<14} {km:>18.4f}")
print(f"{'Centímetros':<14} {cm:>18.4f}")
print(f"{'Milímetros':<14} {mm:>18.4f}")
print(f"{'Polegadas':<14} {polegadas:>18.4f}")
print(f"{'Pés':<14} {pes:>18.4f}")
