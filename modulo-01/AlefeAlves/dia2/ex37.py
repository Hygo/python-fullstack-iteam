import json
from datetime import datetime

class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime) -> None:
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em

    def __repr__(self) -> str:
        return f"Produto(nome={self.nome!r}, preco={self.preco}, criado_em={self.criado_em.isoformat()})"


def produto_para_dict(produto: Produto) -> dict:
    """Converte um Produto em dicionário serializável para JSON.

    Args:
        produto: Instância de Produto a converter.

    Returns:
        Dicionário com nome, preco e criado_em em formato ISO 8601.
    """
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat(),
    }


def dict_para_produto(dados: dict) -> Produto:
    """Reconstrói um Produto a partir de um dicionário.

    Args:
        dados: Dicionário com nome, preco e criado_em (string ISO 8601).

    Returns:
        Instância de Produto reconstruída.
    """
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"]),
    )


produtos = [
    Produto("Notebook Pro",  5999.90, datetime(2025, 1, 10, 9, 0)),
    Produto("Mouse Gamer",    299.90, datetime(2025, 2, 15, 14, 30)),
    Produto("Teclado Mecânico", 489.00, datetime(2025, 3, 22, 11, 45)),
]

json_str = json.dumps([produto_para_dict(p) for p in produtos], indent=2, ensure_ascii=False)
print("=== JSON serializado ===")
print(json_str)

recuperados = [dict_para_produto(d) for d in json.loads(json_str)]
print("\n=== Objetos reconstruídos ===")
for p in recuperados:
    print(f"  {p}")