## 08 – Conversor de Temperatura

celsius = float(input("Digite a temperatura que você quer fazer a conversão: "))

F = (celsius * 9/5) + 32
K = (celsius + 273.15)

print(f"O valor em Celsius é {celsius:.2f}°C")
print(f"O valor em Fahrenheit  é {F:.2f}°F")
print(f"O valor em Kelvin  é {K:.2f}K")