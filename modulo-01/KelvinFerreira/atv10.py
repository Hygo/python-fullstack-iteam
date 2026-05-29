### 🟢 Exercício 10 – Divisão Inteira e Resto
# Dado que um caminhão comporta **850 kg** e cada caixa pesa **32 kg**:
# 1. Calcule quantas caixas **completas** cabem (`//`)
# 2. Calcule o **peso restante** que não completa uma caixa (`%`)
# 3. Exiba os dois valores com mensagens claras

capacidade_caminhao = 850
peso_caixa = 32

caixas_completas = capacidade_caminhao // peso_caixa
peso_restante = capacidade_caminhao % peso_caixa

print("---------------------------------------")
print(f"Caixas completas que cabem: {caixas_completas}")
print(f"Peso restante que não completa uma caixa: {peso_restante} kg")
print("---------------------------------------")
