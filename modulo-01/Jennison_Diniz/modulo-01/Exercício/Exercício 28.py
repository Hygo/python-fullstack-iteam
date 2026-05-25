def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """
    Calcula o montante final utilizando juros compostos.

    Args:
        capital (float): Valor inicial investido. Deve ser não negativo.
        taxa (float): Taxa de juros em porcentagem (%). Deve ser não negativa.
        periodo (int): Número de períodos (meses, anos, etc.) de aplicação.

    Returns:
        float: Montante final após a aplicação dos juros compostos.

    Raises:
        ValueError: Se o capital ou a taxa forem negativos.

    Example:
        >>> calcular_juros_compostos(1000.0, 5.0, 12)
        1795.8563260221301
    """
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if taxa < 0:
        raise ValueError("A taxa de juros não pode ser negativa.")

    return capital * (1 + taxa / 100) ** periodo


# Testando a função
print(calcular_juros_compostos(1000.0, 5.0, 12))  # Saída: 1795.8563260221301
