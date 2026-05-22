def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """Calcula o montante final obtido através de juros compostos.

    Args:
        capital (float): O valor inicial investido.
        taxa (float): A taxa de juros expressa em porcentagem (ex: 5 para 5%).
        periodo (int): O tempo de aplicação em meses/anos compatível com a taxa.

    Returns:
        float: O montante acumulado final.

    Raises:
        ValueError: Se o capital ou a taxa de juros forem negativos.

    Example:
        >>> calcular_juros_compostos(1000.0, 10.0, 2)
        1210.00
    """
    if capital < 0 or taxa < 0:
        raise ValueError("O capital e a taxa não podem ser negativos.")
    return capital * (1 + taxa / 100) ** periodo