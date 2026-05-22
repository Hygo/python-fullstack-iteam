import json
from typing import List, Dict, Any

vendas_json = """
[
    {"mes": "Janeiro",  "produto": "Notebook", "quantidade": 45, "valor_unit": 3200.00},
    {"mes": "Janeiro",  "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro","produto": "Notebook", "quantidade": 38, "valor_unit": 3200.00},
    {"mes": "Fevereiro","produto": "Teclado",  "quantidade": 75, "valor_unit": 149.90},
    {"mes": "Março",    "produto": "Monitor",  "quantidade": 30, "valor_unit": 1200.00},
    {"mes": "Março",    "produto": "Mouse",    "quantidade": 200,"valor_unit": 89.90}
]
"""
dados_vendas = json.loads(vendas_json)

def calcular_total_mes(vendas: List[Dict[str, Any]], mes: str) -> float:
    return sum(item["quantidade"] * item["valor_unit"] for item in vendas if item["mes"].lower() == mes.lower())

def producto_mais_vendido(vendas: List[Dict[str, Any]]) -> str:
    contagem: Dict[str, int] = {}
    for item in vendas:
        contagem[item["produto"]] = contagem.get(item["produto"], 0) + item["quantidade"]
    return max(contagem, key=contagem.get) # type: ignore

def receita_total(vendas: List[Dict[str, Any]]) -> float:
    return sum(item["quantidade"] * item["valor_unit"] for item in vendas)

print(f"Receita em Janeiro: R$ {calcular_total_mes(dados_vendas, 'Janeiro'):.2f}")
print(f"Produto Líder em Qtd: {producto_mais_vendido(dados_vendas)}")
print(f"Receita Global Acumulada: R$ {receita_total(dados_vendas):.2f}")