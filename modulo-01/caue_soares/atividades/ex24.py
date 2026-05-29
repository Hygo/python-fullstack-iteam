def converter_moeda(valor_brl: float) -> tuple[float, float]:
    """
    Converte um valor em reais para dólar americano e euro.

    Args:
        valor_brl (float): Valor em reais (BRL) a ser convertido.

    Returns:
        tuple[float, float]: Tupla com (valor_usd, valor_eur).

    Example:
        >>> converter_moeda(515.00)
        (100.0, 92.29...)
    """
    USD_POR_BRL = 5.15
    EUR_POR_BRL = 5.58

    valor_usd = valor_brl / USD_POR_BRL
    valor_eur = valor_brl / EUR_POR_BRL

    return valor_usd, valor_eur


valor = 1000.00
usd, eur = converter_moeda(valor)

print(f"R$ {valor:.2f}")
print(f"  → USD: $ {usd:.2f}")
print(f"  → EUR: € {eur:.2f}")
