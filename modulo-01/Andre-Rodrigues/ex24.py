from typing import Tuple

def converter_moeda(valor_brl: float) -> Tuple[float, float]:
    """Converte um valor em Reais (BRL) para Dólar (USD) e Euro (EUR).

    Args:
        valor_brl (float): O montante financeiro em reais.

    Returns:
        Tuple[float, float]: Uma tupla contendo (valor_usd, valor_eur).

    Example:
        >>> converter_moeda(100.0)
        (19.41747572815534, 17.921146953405016)
    """
    cotacao_usd = 5.15
    cotacao_eur = 5.58
    
    valor_usd = valor_brl / cotacao_usd
    valor_eur = valor_brl / cotacao_eur
    return valor_usd, valor_eur