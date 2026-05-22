import json

produto = {
    "id": 31,
    "nome": "Mouse Wireless",
    "preco": 149.90,
    "estoque": 20,
    "disponivel": True,
    "categorias": ["Periféricos", "Gamer", "Office"]
}

with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=4, ensure_ascii=False)

with open("produto.json", "r", encoding="utf-8") as f:
    dados_carregados = json.load(f)

print("DADOS DO PRODUTO")
for chave, valor in dados_carregados.items():
    print(f"{chave.title()}: {valor}")