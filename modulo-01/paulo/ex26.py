from typing import Optional, Union, Dict, Any

def buscar_usuario(id_usuario: int, nome: Union[str, None] = None) -> Optional[Dict[str, Any]]:
    """
    Busca os dados de um usuário pelo ID e nome.

    Args:
        id_usuario (int): O ID do usuário. Se for negativo, a função retorna None.
        nome (Union[str, None], opcional): O nome do usuário. Padrão é None.

    Returns:
        Optional[Dict[str, Any]]: Um dicionário com os dados do usuário se o ID for válido,
                                  ou None caso o ID seja negativo.
    """
    if id_usuario < 0:
        return None
    
    return {
        "id": id_usuario,
        "nome": nome,
        "status": "ativo"
    }

print("ID Positivo:", buscar_usuario(1, "Ana"))
print("ID Negativo:", buscar_usuario(-5, "Carlos"))
