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
atualizado_fmt = atualizado.strftime("%d/%m/%Y às %H:%M")

print("╔══════════════════════════════════════╗")
print(f"║  🌤  Boletim Meteorológico             ║")
print("╠══════════════════════════════════════╣")
print(f"║  Cidade    : {dados['cidade']}, {dados['pais']:<22}║")
print(f"║  Condição  : {dados['condicao']:<26}║")
print(f"║  Temperatura atual : {dados['temperatura']['atual']}°C{'':<14}║")
print(f"║  Sensação térmica  : {dados['temperatura']['sensacao']}°C{'':<14}║")
print(f"║  Mínima / Máxima   : {dados['temperatura']['minima']}°C / {dados['temperatura']['maxima']}°C{'':<8}║")
print(f"║  Umidade   : {dados['umidade']}%{'':<25}║")
print(f"║  Vento     : {dados['vento']['velocidade_kmh']} km/h {dados['vento']['direcao']:<20}║")
print(f"║  Atualizado: {atualizado_fmt:<25}║")
print("╚══════════════════════════════════════╝")
