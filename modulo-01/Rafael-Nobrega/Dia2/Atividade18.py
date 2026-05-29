# 18 - Conversão de Unidades Encadeada 

metros = float(input("Poderia digitar uma distancia em metros: "))

km = metros * 0.001
cm = metros * 100.0
mm = metros * 1000.0
polegadas = metros * 39.3701
pes = metros * 3.28084

print("Unidade            |       Valor")
print(f"Metros            |       {metros} m")
print(f"Kilometros        |       {km} Km")
print(f"Centimetros       |      {cm} cm")
print(f"Milimetros        |      {mm} mm")
print(f"Polegadas         |      {polegadas} in")
print(f"Pes               |       {pes} ft")



