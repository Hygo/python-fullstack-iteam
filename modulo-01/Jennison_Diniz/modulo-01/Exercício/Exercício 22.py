def calcular_area(largura: float, altura: float) -> float:
    """
    Calcula a área de um retângulo.

    Args:
        largura (float): Largura do retângulo.
        altura (float): Altura do retângulo.

    Returns:
        float: Área calculada.
    """
    return largura * altura


def formatar_nome(nome: str, sobrenome: str) -> str:
    """
    Formata o nome completo com inicial maiúscula.

    Args:
        nome (str): Primeiro nome.
        sobrenome (str): Sobrenome.

    Returns:
        str: Nome completo formatado.
    """
    return f"{nome} {sobrenome}".title()


def eh_maior_de_idade(idade: int) -> bool:
    """
    Verifica se a pessoa é maior de idade.

    Args:
        idade (int): Idade da pessoa.

    Returns:
        bool: True se for maior de idade, False caso contrário.
    """
    return idade >= 18
