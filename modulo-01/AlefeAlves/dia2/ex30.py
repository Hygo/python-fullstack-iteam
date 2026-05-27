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

pedido = Pedido(
    id_pedido = 123, 
    cliente = "José Bezerra", 
    itens = [
        ItemPedido(
            produto="Arroz", 
            quantidade = 3,
            preco_unitario = 3.99
        ),

        ItemPedido(
            produto="Feijão",
            quantidade=2,
            preco_unitario= 7.75
        )
    ],
    status = "Pago"
)

formatoJSON = json.dumps(pedido, indent=2)

print(f"""
===== PEDIDOS DO CLIENTE {pedido["cliente"]} =====
ID Pedido       : {pedido["id_pedido"]}
Nome do Cliente : {pedido["cliente"]}
Itens do Pedido : {pedido["itens"]}
Status do Pedido: {pedido["status"]}
=======================
""")

#print(formatoJSON)
