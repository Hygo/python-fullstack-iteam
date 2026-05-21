import math

# Definindo as coordenadas dos pontos P1 e P2
x1, y1 = 3, 4
x2, y2 = 7, 1

# Aplicando a fórmula passo a passo: d = √((x2 - x1)² + (y2 - y1)²)
diferenca_x = x2 - x1
diferenca_y = y2 - y1

# Calculando a distância usando math.sqrt para a raiz quadrada
distancia = math.sqrt((diferenca_x ** 2) + (diferenca_y ** 2))

# Exibindo os dados e o resultado formatado com 4 casas decimais
print(f"Ponto 1: ({x1}, {y1})")
print(f"Ponto 2: ({x2}, {y2})")
print("-" * 40)
print(f"A distância entre P1 e P2 é: {distancia:.4f}")