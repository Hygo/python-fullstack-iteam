# Dados do problema
capacidade_caminhao = 850
peso_caixa = 32

# 1. Quantas caixas completas cabem no caminhão (Divisão Inteira)
caixas_completas = capacidade_caminhao // peso_caixa

# 2. O peso restante que não completa uma nova caixa (Resto da Divisão)
peso_restante = capacidade_caminhao % peso_caixa

# Exibindo os resultados com mensagens claras
print(f"Capacidade total do caminhão: {capacidade_caminhao} kg")
print(f"Peso de cada caixa: {peso_caixa} kg")
print("-" * 40)
print(f"O caminhão consegue transportar {caixas_completas} caixas completas.")
print(f"Ficarão sobrando {peso_restante} kg de capacidade que não completam uma caixa.")