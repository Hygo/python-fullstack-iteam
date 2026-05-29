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


# Cria pedido de exemplo
pedido: Pedido = {
    "id_pedido": 5001,
    "cliente": "Fernanda Lima",
    "itens": [
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 3200.00},
        {"produto": "Mouse",    "quantidade": 2, "preco_unitario": 89.90},
        {"produto": "Teclado",  "quantidade": 1, "preco_unitario": 149.90},
    ],
    "status": "aprovado"
}

# Serializa para JSON
json_str = json.dumps(pedido, indent=2, ensure_ascii=False)
print("=== Pedido serializado ===")
print(json_str)

# Calcula total
total = sum(item["quantidade"] * item["preco_unitario"] for item in pedido["itens"])
print(f"\nTotal do pedido: R$ {total:.2f}")
