import json

# String JSON recebida da API
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

# Converter JSON para dicionário
dados = json.loads(resposta_api)

# Criar boletim meteorológico
print("--- Boletim Meteorológico Ambiental ---")
print(f"Cidade: {dados['cidade']} - País: {dados['pais']}")
print(f"Temperatura atual: {dados['temperatura']['atual']} °C")
print(f"Mínima: {dados['temperatura']['minima']} °C | Máxima: {dados['temperatura']['maxima']} °C")
print(f"Sensação térmica: {dados['temperatura']['sensacao']} °C")
print(f"Umidade relativa: {dados['umidade']}%")
print(f"Condição do tempo: {dados['condicao']}")
print(f"Vento: {dados['vento']['velocidade_kmh']} km/h - Direção {dados['vento']['direcao']}")
print(f"Última atualização: {dados['atualizado_em']}")
