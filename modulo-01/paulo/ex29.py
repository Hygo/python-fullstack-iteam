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

print(f"Boletim Meteorológico - {dados['cidade']}, {dados['pais']}")
print(f"Atualizado em: {dados['atualizado_em']}")
print("-" * 35)
print(f"Temperatura atual: {dados['temperatura']['atual']}°C (Sensação de {dados['temperatura']['sensacao']}°C)")
print(f"Mínima: {dados['temperatura']['minima']}°C | Máxima: {dados['temperatura']['maxima']}°C")
print(f"Condição: {dados['condicao']}")
print(f"Umidade: {dados['umidade']}%")
print(f"Vento: {dados['vento']['velocidade_kmh']} km/h direção {dados['vento']['direcao']}")
