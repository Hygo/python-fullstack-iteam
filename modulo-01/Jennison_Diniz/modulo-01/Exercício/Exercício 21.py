def saudacao(nome):
    """
    Retorna uma mensagem de boas-vindas personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: String com a mensagem de boas-vindas.

    Example:
        >>> saudacao("Ana")
        'Olá, Ana! Seja bem-vinda ao curso.'
    """
    return f"Olá, {nome}! Seja bem-vinda ao curso."


# Chamando a função com 3 nomes diferentes
print(saudacao("Ana"))
print(saudacao("Carlos"))
print(saudacao("Mariana"))
