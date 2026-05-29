def calcular_juros_compostos(capital: float, taxa: float, periodo: int) -> float:
    """Calcula o montante final com juros compostos.

    Aplica a fórmula M = C × (1 + i/100)^t, onde C é o capital inicial,
    i é a taxa percentual ao período e t é o número de períodos.

    Args:
        capital (float): Capital inicial investido, em reais. Deve ser positivo.
        taxa (float): Taxa de juros por período, em porcentagem (ex: 2.5 para 2,5%).
            Deve ser positiva.
        periodo (int): Número de períodos (ex: meses). Deve ser maior que zero.

    Returns:
        float: Montante final após a aplicação dos juros compostos.

    Raises:
        ValueError: Se `capital` for negativo ou zero.
        ValueError: Se `taxa` for negativa.

    Example:
        >>> calcular_juros_compostos(1000.0, 1.5, 12)
        1195.618...
    """
    if capital <= 0:
        raise ValueError("O capital deve ser positivo.")
    if taxa < 0:
        raise ValueError("A taxa não pode ser negativa.")

    return capital * (1 + taxa / 100) ** periodo


# Demonstração
montante = calcular_juros_compostos(1000.0, 1.5, 12)
print(f"Montante após 12 meses a 1,5% a.m.: R$ {montante:.2f}")

# Teste de erro
try:
    calcular_juros_compostos(-500, 1.5, 12)
except ValueError as e:
    print(f"Erro capturado: {e}")
