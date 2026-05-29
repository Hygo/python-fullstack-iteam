from typing import Optional, Union


def buscar_usuario(id: int, nome: Optional[str] = None) -> Optional[dict]:
    """
    Busca um usuário pelo ID e nome opcional.

    Args:
        id (int): Identificador único do usuário. Deve ser positivo.
        nome (Optional[str]): Nome do usuário. Pode ser None se desconhecido.

    Returns:
        Optional[dict]: Dicionário com os dados do usuário, ou None se o
            id for negativo (inválido).

    Example:
        >>> buscar_usuario(1, "Ana")
        {'id': 1, 'nome': 'Ana', 'status': 'encontrado'}
        >>> buscar_usuario(-1)
        None
    """
    if id < 0:
        return None

    return {
        "id": id,
        "nome": nome if nome is not None else "Desconhecido",
        "status": "encontrado"
    }


# Testes
print(buscar_usuario(1, "Ana"))
print(buscar_usuario(2))
print(buscar_usuario(-5, "Carlos"))
