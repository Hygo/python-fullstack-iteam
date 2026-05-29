### 🔴 Exercício 16 – Distância entre Dois Pontos
# Fórmula: d = √((x2 - x1)² + (y2 - y1)²)
# Defina P1 = (3, 4) e P2 = (7, 1), calcule com math.sqrt e exiba com 4 casas decimais.

import math

p1 = (3, 4)
p2 = (7, 1)

distancia = math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(f"P1: {p1}")
print(f"P2: {p2}")
print(f"Distância entre P1 e P2: {distancia:.4f}")
