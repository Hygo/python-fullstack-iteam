import math

x1, y1 = 3, 4
x2, y2 = 7, 1

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"P1 = ({x1}, {y1})")
print(f"P2 = ({x2}, {y2})")
print(f"Distância entre os pontos: {distancia:.4f}")
