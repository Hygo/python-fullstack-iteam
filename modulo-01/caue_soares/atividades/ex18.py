metros = float(input("Digite a distância em metros: "))

km = metros / 1000
cm = metros * 100
mm = metros * 1000
polegadas = metros * 39.3701
pes = metros * 3.28084

print(f"\n{'Unidade':<12} {'Valor':>15}")
print("-" * 28)
print(f"{'Metros':<12} {metros:>15.4f} m")
print(f"{'Quilômetros':<12} {km:>15.6f} km")
print(f"{'Centímetros':<12} {cm:>15.2f} cm")
print(f"{'Milímetros':<12} {mm:>15.2f} mm")
print(f"{'Polegadas':<12} {polegadas:>15.4f} in")
print(f"{'Pés':<12} {pes:>15.4f} ft")
