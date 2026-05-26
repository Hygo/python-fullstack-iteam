caminhao = 850 
caixa = 32

caixasQueCabem = caminhao // caixa
pesoSobrando = caminhao % caixa

print(f"No caminhão cabem no total {caixasQueCabem} caixas de 32kg.")
print(f"Peso sobrando: {pesoSobrando}.")