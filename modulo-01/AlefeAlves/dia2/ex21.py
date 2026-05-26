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
    return (f'Olá, {nome}! Seja bem-vindo/a ao curso.')

print(saudacao("Álefe"))
print(saudacao("Amanda"))
print(saudacao("Luciano"))