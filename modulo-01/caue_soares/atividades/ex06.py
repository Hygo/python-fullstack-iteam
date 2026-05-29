ano_atual = 2025
temperatura = 28.5
cidade = "Manaus"
chovendo = False
previsao = None
string_vazia = ""

variaveis = [ano_atual, temperatura, cidade, chovendo, previsao, string_vazia]

for v in variaveis:
    print(f"{repr(v)} → {type(v)}")
