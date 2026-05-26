def converter_moeda( valor_brl : float ) -> tuple :
    """
    Retorna uma tupla com dois valores (float), contendo o valor em dólar e em euros.

    Args:
        valor_brl (float): Valor em reais (BRL).

    Returns:
        tuple: Tupla com as conversões para dólar e euros, respectivamente.

    Example: 
        >>> converter_moeda(10)
        (1.9417475728155338, 1.7921146953405018)
    """
    valor_usd = valor_brl / 5.15
    valor_eur = valor_brl / 5.58

    return (valor_usd, valor_eur)

print(converter_moeda(10))