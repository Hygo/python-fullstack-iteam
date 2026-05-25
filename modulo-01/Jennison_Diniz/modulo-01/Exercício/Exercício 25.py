import json

# Criando o dicionário de produto
produto = {
    "id": 101,
    "nome": "Smartphone X",
    "preco": 1999.90,
    "estoque": 35,
    "disponivel": True,
    "categorias": ["Eletrônicos", "Celulares", "Promoção"]
}

# Salvando em produto.json
with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=2, ensure_ascii=False)

# Lendo o arquivo de volta
with open("produto.json", "r", encoding="utf-8") as f:
    produto_lido = json.load(f)

# Exibindo cada campo com etiqueta
print("--- Dados do Produto ---")
print(f"ID: {produto_lido['id']}")
print(f"Nome: {produto_lido['nome']}")
print(f"Preço: R$ {produto_lido['preco']:.2f}")
print(f"Estoque: {produto_lido['estoque']} unidades")
print(f"Disponível: {'Sim' if produto_lido['disponivel'] else 'Não'}")
print(f"Categorias: {', '.join(produto_lido['categorias'])}")
