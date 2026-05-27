def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """
    Retorna um float com o valor dos juros compostos calculado.

    Args:
        capital (float): Valor investido em reais. (Positivo)
        taxa (float): Taxa de juros em porcento. (Positivo)
        periodo (int): Período do investimento em meses. (Positivo)

    Returns:
        float: Juro composto total do investimento.

    Raises: 
        ValueError: Se capital ou taxa forem negativos.
        
    Example:
        >>> calcular_juros_compostos(1000.0, 2.0, 12)
        1268.24...
    """
    if capital < 0 or taxa < 0:
        return ValueError("Capital e taxa devem ser positivos")

    return capital * (1 + taxa / 100) ** periodo
