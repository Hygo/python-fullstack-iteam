import json
from datetime import datetime
from typing import Dict, Any, List

class Produto:
    def __init__(self, nome: str, preco: float, criado_em: datetime):
        self.nome = nome
        self.preco = preco
        self.criado_em = criado_em

def produto_para_dict(produto: Produto) -> Dict[str, Any]:
    return {
        "nome": produto.nome,
        "preco": produto.preco,
        "criado_em": produto.criado_em.isoformat()
    }

def dict_para_produto(dados: Dict[str, Any]) -> Produto:
    return Produto(
        nome=dados["nome"],
        preco=dados["preco"],
        criado_em=datetime.fromisoformat(dados["criado_em"])
    )

produtos_lista = [
    Produto("Cadeira Gamer", 1200.0, datetime.now()),
    Produto("Mesa Ergonômica", 850.0, datetime.now())
]


dicionarios = [produto_para_dict(p) for p in produtos_lista]
json_string = json.dumps(dicionarios, indent=2)


dados_voltou = json.loads(json_string)
objetos_recuperados = [dict_para_produto(d) for d in dados_voltou]

print(f"Classe recuperada com sucesso: {type(objetos_recuperados[0])}")
print(f"Data de criação nativa convertida: {objetos_recuperados[0].criado_em}")