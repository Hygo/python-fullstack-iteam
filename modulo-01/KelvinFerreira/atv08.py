### 🟢 Exercício 08 – Conversor de Temperatura
# Escreva um script que converta uma temperatura de **Celsius para Fahrenheit** e para **Kelvin**.
# Fórmulas:
# - `F = (C × 9/5) + 32`
# - `K = C + 273.15`
# Use o valor `36.5°C` e exiba os três valores formatados.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

temp_celsius = 36.5
temp_fahr = celsius_para_fahrenheit(temp_celsius)
temp_kelvin = celsius_para_kelvin(temp_celsius)
print(f"{temp_celsius}°C é igual a {temp_fahr:.1f}°F e {temp_kelvin:.2f}K")