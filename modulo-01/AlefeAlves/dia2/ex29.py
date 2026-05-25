import json

resposta_api = """
{
    "cidade": "Manaus",
    "pais": "BR",
    "temperatura": {
        "atual": 32.4,
        "minima": 26.1,
        "maxima": 35.8,
        "sensacao": 38.2
    },
    "umidade": 87,
    "condicao": "Parcialmente nublado",
    "vento": { "velocidade_kmh": 12, "direcao": "NE" },
    "atualizado_em": "2025-01-15T14:30:00"
}
"""

dados = json.loads(resposta_api)

print(f"""
===== RELATÓRIO METEREOLÓGICO DA CIDADE DE {dados["cidade"]} =====
Cidade                     : {dados["cidade"]}
Pais                       : {dados["pais"]}
Temperatura Atual          : {dados["temperatura"]["atual"]} ºC
Temperatura Mínima         : {dados["temperatura"]["minima"]} ºC
Temperatura Máxima         : {dados["temperatura"]["maxima"]} ºC
Temperatura Sensação       : {dados["temperatura"]["sensacao"]} ºC
Umidade                    : {dados["umidade"]}
Condição                   : {dados["condicao"]}
Velocidade do Vento em KM/H: {dados["vento"]["velocidade_kmh"]} KM/H
Direção do Vento           : {dados["vento"]["direcao"]}
=======================
""")