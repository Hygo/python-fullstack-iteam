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
    "id_pedido": 2025,
    "cliente": "João Silva",
    "itens": [
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 3500.00},
        {"produto": "Mouse Gamer", "quantidade": 2, "preco_unitario": 150.00},
        {"produto": "Headset", "quantidade": 1, "preco_unitario": 300.00}
    ],
    "status": "Em processamento"
}

# Serializando para JSON
pedido_json = json.dumps(pedido_exemplo, indent=2, ensure_ascii=False)

# Exibindo JSON formatado
print("--- Pedido em JSON ---")
print(pedido_json)
