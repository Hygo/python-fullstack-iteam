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

print(f"=BOLETIM METEOROLÓGICO: {dados['cidade'].upper()} ({dados['pais']})=")
print(f"Condição Atual: {dados['condicao']}")
print(f"Temperatura   : {dados['temperatura']['atual']}°C (Sensação de {dados['temperatura']['sensacao']}°C)")
print(f"Extremas      : Mínima de {dados['temperatura']['minima']}°C | Máxima de {dados['temperatura']['maxima']}°C")
print(f"Umidade do Ar : {dados['umidade']}%")
print(f"Vento         : {dados['vento']['velocidade_kmh']} km/h vindo do {dados['vento']['direcao']}")
print(f"Atualizado em : {dados['atualizado_em']}")