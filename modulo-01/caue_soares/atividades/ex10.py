capacidade_kg = 850
peso_caixa = 32

caixas_completas = capacidade_kg // peso_caixa
peso_restante = capacidade_kg % peso_caixa

print(f"Caixas completas que cabem: {caixas_completas}")
print(f"Peso restante sem completar uma caixa: {peso_restante} kg")
