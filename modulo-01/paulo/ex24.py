from typing import Tuple

def converter_moeda(valor_reais: float) -> Tuple[float, float]:
    """
    Converte um valor em reais para dólar e euro.

    Args:
        valor_reais (float): O valor em reais (BRL) a ser convertido.

    Returns:
        Tuple[float, float]: Uma tupla contendo o valor em dólares (USD) e em euros (EUR).

    Example:
        >>> converter_moeda(100.0)
        (19.41747572815534, 17.92114695340502)
    """
    cotacao_usd = 5.15
    cotacao_eur = 5.58

    usd = valor_reais / cotacao_usd
    eur = valor_reais / cotacao_eur

    return usd, eur
