def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """
    Calcula o montante final usando juros compostos.

    Args:
        capital (float): O valor do capital inicial.
        taxa (float): A taxa de juros (em porcentagem).
        periodo (int): O número de períodos de tempo.

    Returns:
        float: O montante final após a aplicação dos juros compostos.

    Raises:
        ValueError: Se o capital ou a taxa forem negativos.

    Example:
        >>> calcular_juros_compostos(1000.0, 5.0, 12)
        1795.85632602213
    """
    if capital < 0 or taxa < 0:
        raise ValueError("Capital e taxa não podem ser negativos.")
        
    return capital * (1 + taxa / 100) ** periodo

print(calcular_juros_compostos(1000.0, 5.0, 12))
