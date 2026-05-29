### 🔴 Exercício 29 – Parser de JSON de API Meteorológica
# Faça o parse da string JSON abaixo e exiba um boletim meteorológico amigável.

import json
from datetime import datetime

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
atualizado = datetime.fromisoformat(dados["atualizado_em"])

print("=" * 40)
print(f"  BOLETIM METEOROLÓGICO")
print("=" * 40)
print(f"  {dados['cidade']}, {dados['pais']}")
print(f"  {dados['condicao']}")
print("-" * 40)
print(f"  Temperatura atual : {dados['temperatura']['atual']}°C")
print(f"  Sensação térmica  : {dados['temperatura']['sensacao']}°C")
print(f"  Mínima / Máxima   : {dados['temperatura']['minima']}°C / {dados['temperatura']['maxima']}°C")
print(f"  Umidade relativa  : {dados['umidade']}%")
print(f"  Vento             : {dados['vento']['velocidade_kmh']} km/h ({dados['vento']['direcao']})")
print("-" * 40)
print(f"  Atualizado em: {atualizado.strftime('%d/%m/%Y às %H:%M')}")
print("=" * 40)
