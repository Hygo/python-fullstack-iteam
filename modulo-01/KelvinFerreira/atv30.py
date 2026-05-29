### 🔴 Exercício 30 – Typing Avançado: TypedDict
# Use TypedDict para criar estruturas tipadas de um pedido de e-commerce.

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


pedido: Pedido = {
    "id_pedido": 5001,
    "cliente": "Kelvin Araújo",
    "itens": [
        {"produto": "Notebook", "quantidade": 1, "preco_unitario": 4599.90},
        {"produto": "Mouse sem fio", "quantidade": 2, "preco_unitario": 129.90},
        {"produto": "Mousepad XL", "quantidade": 1, "preco_unitario": 89.90},
    ],
    "status": "Aguardando pagamento"
}

json_pedido = json.dumps(pedido, indent=2, ensure_ascii=False)

print("Pedido serializado em JSON:")
print(json_pedido)

total = sum(item["quantidade"] * item["preco_unitario"] for item in pedido["itens"])
print(f"\nTotal do pedido #{pedido['id_pedido']}: R$ {total:.2f}")
print(f"Status: {pedido['status']}")
