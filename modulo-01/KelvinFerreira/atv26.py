### 🟡 Exercício 26 – Typing com Optional e Union
# Escreva a função buscar_usuario que receba id (int) e nome que pode ser str ou None.
# Retorne dicionário com os dados ou None se o id for negativo.

from typing import Optional, Union, Dict, Any


def buscar_usuario(id: int, nome: Union[str, None]) -> Optional[Dict[str, Any]]:
    """
    Busca um usuário pelo id e nome fornecidos.

    Args:
        id (int): Identificador do usuário. Deve ser positivo.
        nome (Union[str, None]): Nome do usuário ou None se desconhecido.

    Returns:
        Optional[Dict[str, Any]]: Dicionário com os dados do usuário, ou None se
        o id for negativo.

    Example:
        >>> buscar_usuario(1, "Ana")
        {'id': 1, 'nome': 'Ana', 'ativo': True}
        >>> buscar_usuario(-1, None)
        None
    """
    if id < 0:
        return None
    return {"id": id, "nome": nome if nome else "Desconhecido", "ativo": True}


print(buscar_usuario(1, "Ana"))
print(buscar_usuario(42, None))
print(buscar_usuario(-5, "Carlos"))
