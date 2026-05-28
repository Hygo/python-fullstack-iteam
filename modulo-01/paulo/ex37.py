import json
from datetime import datetime

class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime = None):
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em if criado_em else datetime.now()

def produto_para_dict(produto: 'Produto') -> dict:
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat()
    }

def dict_para_produto(dados: dict) -> 'Produto':
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"])
    )

produtos = [
    Produto("Mouse", 50.0),
    Produto("Teclado", 150.0),
    Produto("Monitor", 800.0)
]

# Serialização
produtos_dict = [produto_para_dict(p) for p in produtos]
json_str = json.dumps(produtos_dict, indent=4)
print("JSON Serializado:")
print(json_str)

# Desserialização
dados_lidos = json.loads(json_str)
produtos_desserializados = [dict_para_produto(d) for d in dados_lidos]

print("\nProdutos Desserializados:")
for p in produtos_desserializados:
    print(f"- {p.nome} (R$ {p.preco:.2f}) criado em {p.criado_em}")
