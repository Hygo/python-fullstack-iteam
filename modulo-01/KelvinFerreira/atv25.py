### 🟡 Exercício 25 – Salvando Dados em JSON
# Crie um dicionário de produto de e-commerce, salve em produto.json e leia de volta.

import json

produto = {
    "id": 101,
    "nome": "Teclado Mecânico RGB",
    "preco": 349.90,
    "estoque": 42,
    "disponivel": True,
    "categorias": ["periféricos", "informática", "gaming"]
}

with open("produto.json", "w", encoding="utf-8") as f:
    json.dump(produto, f, indent=2, ensure_ascii=False)

print("Arquivo produto.json salvo com sucesso.\n")

with open("produto.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(f"ID         : {dados['id']}")
print(f"Nome       : {dados['nome']}")
print(f"Preço      : R$ {dados['preco']:.2f}")
print(f"Estoque    : {dados['estoque']} unidades")
print(f"Disponível : {'Sim' if dados['disponivel'] else 'Não'}")
print(f"Categorias : {', '.join(dados['categorias'])}")
