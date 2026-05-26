import json

produto = {
    "id": 1,
    "nome": "Arroz",
    "preco": 3.89,
    "estoque": 500,
    "disponivel": True,
    "categorias": ["Alimentação",]
}

with open("produtos.json", "w") as f:
    json.dump(produto, f, indent=4)

with open("produtos.json", "r") as f:
    produto = json.load(f)

print(f"""
===== IMPRIMINDO PRODUTO =====
ID do Produto             : {produto["id"]}
Nome do Produto           : {produto["nome"]}
Preço do Produto          : R$ {produto["preco"]}
Estoque do Produto        : {produto["estoque"]}
Disponibilidade do Produto: {produto["disponivel"]}
Categorias do Produto     : {produto["categorias"]}
=======================
""")


