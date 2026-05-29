### 🟡 Exercício 28 – Docstring Google Style + Juros Compostos
# Reescreva a função com type hints e docstring no padrão Google Style.


def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """
    Calcula o montante final com juros compostos.

    Args:
        capital (float): Valor inicial investido em reais. Deve ser positivo.
        taxa (float): Taxa de juros por período em percentual (ex: 2.5 para 2,5%).
                      Deve ser positiva.
        periodo (int): Número de períodos de capitalização.

    Returns:
        float: Montante final após a aplicação dos juros compostos.

    Raises:
        ValueError: Se capital ou taxa forem negativos.

    Example:
        >>> calcular_juros_compostos(1000.0, 2.0, 12)
        1268.24...
    """
    if capital < 0:
        raise ValueError("O capital não pode ser negativo.")
    if taxa < 0:
        raise ValueError("A taxa não pode ser negativa.")
    return capital * (1 + taxa / 100) ** periodo


capital = 5000.0
taxa = 1.5
periodo = 24
montante = calcular_juros_compostos(capital, taxa, periodo)

print(f"Capital inicial : R$ {capital:.2f}")
print(f"Taxa mensal     : {taxa}%")
print(f"Período         : {periodo} meses")
print(f"Montante final  : R$ {montante:.2f}")
print(f"Juros ganhos    : R$ {montante - capital:.2f}")
