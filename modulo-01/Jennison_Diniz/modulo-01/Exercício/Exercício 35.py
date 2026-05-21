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

# Converter JSON para lista de dicionários
vendas: List[Dict[str, Any]] = json.loads(vendas_json)


def calcular_total_mes(vendas: List[Dict[str, Any]], mes: str) -> float:
    """
    Calcula o total de vendas em um determinado mês.

    Args:
        vendas (List[Dict[str, Any]]): Lista de registros de vendas.
        mes (str): Nome do mês a ser analisado.

    Returns:
        float: Valor total das vendas no mês.
    """
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas if v["mes"] == mes)


def produto_mais_vendido(vendas: List[Dict[str, Any]]) -> str:
    """
    Identifica o produto mais vendido em quantidade.

    Args:
        vendas (List[Dict[str, Any]]): Lista de registros de vendas.

    Returns:
        str: Nome do produto mais vendido.
    """
    totais: Dict[str, int] = {}
    for v in vendas:
        totais[v["produto"]] = totais.get(v["produto"], 0) + v["quantidade"]
    return max(totais, key=totais.get)


def receita_total(vendas: List[Dict[str, Any]]) -> float:
    """
    Calcula a receita total de todas as vendas.

    Args:
        vendas (List[Dict[str, Any]]): Lista de registros de vendas.

    Returns:
        float: Receita total.
    """
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas)


# --- Demonstração ---
print("--- Relatório de Vendas ---")
print(f"Total em Janeiro: R$ {calcular_total_mes(vendas, 'Janeiro'):.2f}")
print(f"Total em Fevereiro: R$ {calcular_total_mes(vendas, 'Fevereiro'):.2f}")
print(f"Total em Março: R$ {calcular_total_mes(vendas, 'Março'):.2f}")
print(f"Produto mais vendido: {produto_mais_vendido(vendas)}")
print(f"Receita total: R$ {receita_total(vendas):.2f}")
