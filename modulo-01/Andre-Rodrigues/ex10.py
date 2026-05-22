capacidade_caminhao = 850
peso_caixa = 32

caixas_completas = capacidade_caminhao // peso_caixa
peso_restante = capacidade_caminhao % peso_caixa

print(f"Cabem {caixas_completas} caixas completas no caminhão.")
print(f"Sobram {peso_restante} kg de espaço livre.")