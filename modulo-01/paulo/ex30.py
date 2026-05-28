import json
from typing import TypedDict, List

class ItemPedido(TypedDict):
    produto: str
    quantidade: int
    preco_unitario: float

class Pedido(TypedDict):
    id_pedido: int
    cliente: str
    itens: List[ItemPedido]
    status: str

# Criando um pedido de exemplo
pedido_exemplo: Pedido = {
    "id_pedido": 12345,
    "cliente": "Marcos Silva",
    "itens": [
        {"produto": "Mousepad", "quantidade": 2, "preco_unitario": 45.90},
        {"produto": "Teclado", "quantidade": 1, "preco_unitario": 299.90}
    ],
    "status": "Em processamento"
}

# Serializando para JSON
pedido_json = json.dumps(pedido_exemplo, indent=4, ensure_ascii=False)

print("Pedido Serializado:")
print(pedido_json)
