metros = float(input("Informe a distância em metros: "))

print(f"""
===== CONVERSOR DE MEDIDAS =====
Metros (Original): [{metros}]
Quilômetros (km) : [{metros / 1000}]
Centímetros (cm) : [{metros * 100}]
Milímetros (mm)  : [{metros * 1000}]
Polegadas        : [{metros * 39.37}]
Pés              : [{metros * 3.281}]
=======================
""")