### 🟡 Exercício 24 – Função Documentada com Typing: Conversor de Moeda
# Escreva a função converter_moeda com type hints completos e docstring.
# Cotações: 1 USD = 5.15 BRL | 1 EUR = 5.58 BRL

from typing import Tuple

USD_POR_BRL = 5.15
EUR_POR_BRL = 5.58


def converter_moeda(valor_brl: float) -> Tuple[float, float]:
    """
    Converte um valor em reais para dólar americano e euro.

    Args:
        valor_brl (float): Valor em reais a ser convertido.

    Returns:
        Tuple[float, float]: Tupla (valor_usd, valor_eur) com os valores convertidos.

    Example:
        >>> converter_moeda(515.0)
        (100.0, 92.29...)
    """
    valor_usd = valor_brl / USD_POR_BRL
    valor_eur = valor_brl / EUR_POR_BRL
    return valor_usd, valor_eur


valor = 1000.0
usd, eur = converter_moeda(valor)
print(f"R$ {valor:.2f} equivale a:")
print(f"  USD: $ {usd:.2f}")
print(f"  EUR: € {eur:.2f}")
