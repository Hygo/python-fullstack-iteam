import json

produto = {
    "id": 101,
    "nome": "Teclado Mecânico RGB",
    "preco": 349.90,
    "estoque": 42,
    "disponivel": True,
    "categorias": ["Periféricos", "Informática", "Gamer"]
}

# Salva no arquivo
with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=2, ensure_ascii=False)

print("Arquivo produto.json salvo com sucesso!\n")

# Lê o arquivo de volta
with open("produto.json", "r", encoding="utf-8") as f:
    produto_lido = json.load(f)

print(f"ID         : {produto_lido['id']}")
print(f"Nome       : {produto_lido['nome']}")
print(f"Preço      : R$ {produto_lido['preco']:.2f}")
print(f"Estoque    : {produto_lido['estoque']} unidades")
print(f"Disponível : {'Sim' if produto_lido['disponivel'] else 'Não'}")
print(f"Categorias : {', '.join(produto_lido['categorias'])}")
