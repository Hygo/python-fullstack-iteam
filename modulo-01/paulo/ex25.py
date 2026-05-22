import json

produto = {
    "id": 101,
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 25,
    "disponivel": True,
    "categorias": ["Periféricos", "Informática", "Gamer"]
}

# Salva em produto.json
with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=4, ensure_ascii=False)

# Lê de produto.json
with open("produto.json", "r", encoding="utf-8") as f:
    produto_lido = json.load(f)

print("ID:", produto_lido["id"])
print("Nome:", produto_lido["nome"])
print("Preço:", produto_lido["preco"])
print("Estoque:", produto_lido["estoque"])
print("Disponível:", produto_lido["disponivel"])
print("Categorias:", ", ".join(produto_lido["categorias"]))
