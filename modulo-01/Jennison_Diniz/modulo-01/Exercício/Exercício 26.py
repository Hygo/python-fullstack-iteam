from typing import Optional, Union, Dict

def buscar_usuario(id: int, nome: Optional[str]) -> Optional[Dict[str, Union[int, str]]]:
    """
    Busca um usuário pelo ID e nome.

    Args:
        id (int): Identificador único do usuário.
        nome (Optional[str]): Nome do usuário. Pode ser uma string ou None.

    Returns:
        Optional[Dict[str, Union[int, str]]]: 
            - Um dicionário com os dados do usuário se o ID for positivo.
            - None se o ID for negativo.

    Example:
        >>> buscar_usuario(1, "Maria")
        {'id': 1, 'nome': 'Maria'}

        >>> buscar_usuario(-5, "João")
        None
    """
    if id < 0:
        return None
    
    return {"id": id, "nome": nome if nome is not None else "Desconhecido"}


# Testando a função
print(buscar_usuario(1, "Maria"))     # {'id': 1, 'nome': 'Maria'}
print(buscar_usuario(2, None))        # {'id': 2, 'nome': 'Desconhecido'}
print(buscar_usuario(-5, "João"))     # None
