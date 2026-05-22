metros = float(input("Digite uma distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084

print(f"{'Metros':<15} | {metros:>10.2f}")
print("-" * 30)
print(f"{'Quilômetros':<15} | {km:>10.4f}")
print(f"{'Centímetros':<15} | {cm:>10.2f}")
print(f"{'Milímetros':<15} | {mm:>10.2f}")
print(f"{'Polegadas':<15} | {polegadas:>10.2f}")
print(f"{'Pés':<15} | {pes:>10.2f}")
