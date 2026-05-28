# P1 = (3 ,4) - (x1, y1)
# P2 = (7 ,1) - (x2, y2)

import math

P1 = (3, 4) # (x1, y1)
P2 = (7, 1) # (x2, y2)

d = math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

print(f"P1 = {P1}")
print(f"P2 = {P2}")
print(f"Distância = {d:.4f}")