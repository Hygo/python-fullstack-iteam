import typing

def buscar_usuario(id: (int), nome: typing.Optional[str] = None) -> typing.Union[dict, None]:
    """
    Retorna um dicionário com os dados do usuário ou None se o usuário não existir.

    Args:
        id (int): Id do usuário em questão.
        nome (str): Nome do usuário a procurar.

    Returns:
        dict: Dicionário contendo as informações do usuário procurado.
        None: Caso o id informado seja negativo.

    Example:
        >>> buscar_usuario(1, "Ana")
        {"id": 1, "nome": "Ana", "email": "ana@gmail.com" }
    """
    if id < 0: 
        return None
    
    return {"id": 1, "nome": "Ana", "email": "ana@gmail.com" }

    
