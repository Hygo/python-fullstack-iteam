import json

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
vendas = json.loads(vendas_json)

def calcular_total_mes(vendas: list, mes: str) -> float:
    return sum(item["quantidade"] * item["valor_unit"] for item in vendas if item["mes"] == mes)

def produto_mais_vendido(vendas: list) -> str:
    quantidades = {}
    for item in vendas:
        quantidades[item["produto"]] = quantidades.get(item["produto"], 0) + item["quantidade"]
    return max(quantidades, key=quantidades.get) if quantidades else ""

def receita_total(vendas: list) -> float:
    return sum(item["quantidade"] * item["valor_unit"] for item in vendas)

print(f"Total Janeiro: R$ {calcular_total_mes(vendas, 'Janeiro'):.2f}")
print(f"Produto mais vendido: {produto_mais_vendido(vendas)}")
print(f"Receita Total: R$ {receita_total(vendas):.2f}")
