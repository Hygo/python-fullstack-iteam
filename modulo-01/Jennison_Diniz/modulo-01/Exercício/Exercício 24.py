def converter_moeda(valor_brl: float) -> tuple[float, float]:
    """
    Converte um valor em reais (BRL) para dólar (USD) e euro (EUR).

    Args:
        valor_brl (float): Valor em reais a ser convertido.

    Returns:
        tuple[float, float]: Uma tupla contendo:
            - valor_usd (float): Valor convertido em dólares.
            - valor_eur (float): Valor convertido em euros.

    Example:
        >>> converter_moeda(100.0)
        (19.42, 17.92)
    """
    cotacao_usd = 5.15
    cotacao_eur = 5.58

    valor_usd = valor_brl / cotacao_usd
    valor_eur = valor_brl / cotacao_eur

    return valor_usd, valor_eur


# Testando a função
valor = 100.0
usd, eur = converter_moeda(valor)
print(f"Valor em BRL: R$ {valor:.2f}")
print(f"Convertido em USD: $ {usd:.2f}")
print(f"Convertido em EUR: € {eur:.2f}")
