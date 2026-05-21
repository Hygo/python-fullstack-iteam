import json
from datetime import datetime
from typing import List, Dict

class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime):
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome}, preco={self.preco}, criado_em={self.criado_em.isoformat()})"


def produto_para_dict(produto: Produto) -> Dict[str, str | float]:
    """
    Converte um objeto Produto em dicionário serializável para JSON.

    Args:
        produto (Produto): Objeto Produto.

    Returns:
        dict: Dicionário com os dados do produto.
    """
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat()
    }


def dict_para_produto(dados: Dict[str, str | float]) -> Produto:
    """
    Converte um dicionário em objeto Produto.

    Args:
        dados (dict): Dicionário com os dados do produto.

    Returns:
        Produto: Objeto Produto reconstruído.
    """
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"])
    )


# --- Demonstração ---
produtos: List[Produto] = [
    Produto("Notebook", 3500.00, datetime.now()),
    Produto("Mouse Gamer", 150.00, datetime.now()),
    Produto("Monitor", 1200.00, datetime.now())
]

# Serializar lista de produtos para JSON
produtos_dict = [produto_para_dict(p) for p in produtos]
produtos_json = json.dumps(produtos_dict, indent=2, ensure_ascii=False)
print("--- Produtos Serializados ---")
print(produtos_json)

# Desserializar de volta para objetos Produto
produtos_lidos = json.loads(produtos_json)
produtos_objetos = [dict_para_produto(d) for d in produtos_lidos]

print("\n--- Produtos Desserializados ---")
for p in produtos_objetos:
    print(p)
