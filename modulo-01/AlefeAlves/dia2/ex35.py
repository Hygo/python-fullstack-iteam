import json

vendas_json = """
[
    {"mes": "Janeiro",   "produto": "Notebook", "quantidade": 45,  "valor_unit": 3200.00},
    {"mes": "Janeiro",   "produto": "Mouse",    "quantidade": 120, "valor_unit": 89.90},
    {"mes": "Fevereiro", "produto": "Notebook", "quantidade": 38,  "valor_unit": 3200.00},
    {"mes": "Fevereiro", "produto": "Teclado",  "quantidade": 75,  "valor_unit": 149.90},
    {"mes": "Março",     "produto": "Monitor",  "quantidade": 30,  "valor_unit": 1200.00},
    {"mes": "Março",     "produto": "Mouse",    "quantidade": 200, "valor_unit": 89.90}
]
"""


def calcular_total_mes(vendas: list, mes: str) -> float:
    """Calcula a receita total de um mês específico.

    Args:
        vendas: Lista de dicionários com os dados de vendas.
        mes: Nome do mês a filtrar (ex: "Janeiro").

    Returns:
        Soma de quantidade × valor_unit para o mês informado.
    """
    return sum(
        v["quantidade"] * v["valor_unit"]
        for v in vendas
        if v["mes"] == mes
    )


def produto_mais_vendido(vendas: list) -> str:
    """Retorna o nome do produto com maior quantidade total vendida.

    Args:
        vendas: Lista de dicionários com os dados de vendas.

    Returns:
        Nome do produto líder em quantidade.
    """
    totais: dict[str, int] = {}
    for v in vendas:
        totais[v["produto"]] = totais.get(v["produto"], 0) + v["quantidade"]
    return max(totais, key=lambda p: totais[p])


def receita_total(vendas: list) -> float:
    """Calcula a receita total de todas as vendas.

    Args:
        vendas: Lista de dicionários com os dados de vendas.

    Returns:
        Soma geral de quantidade × valor_unit.
    """
    return sum(v["quantidade"] * v["valor_unit"] for v in vendas)


vendas = json.loads(vendas_json)

print("========== RELATÓRIO DE VENDAS ==========")
for mes in ("Janeiro", "Fevereiro", "Março"):
    total = calcular_total_mes(vendas, mes)
    print(f"  {mes:<12}: R$ {total:>12,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

print(f"\nProduto mais vendido : {produto_mais_vendido(vendas)}")
total_geral = receita_total(vendas)
print(f"Receita total        : R$ {total_geral:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
print("==========================================")