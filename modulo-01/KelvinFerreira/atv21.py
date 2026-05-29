### 🟢 Exercício 21 – Sua Primeira Função com Docstring
# Escreva uma função `saudacao` que receba um nome e retorne uma string de boas-vindas,
# com docstring completa.

def saudacao(nome: str) -> str:
    """
    Retorna uma mensagem de boas-vindas personalizada.

    Args:
        nome (str): Nome da pessoa a ser saudada.

    Returns:
        str: String com a mensagem de boas-vindas.

    Example:
        >>> saudacao("Ana")
        'Olá, Ana! Seja bem-vinda ao curso.'
    """
    return f"Olá, {nome}! Seja bem-vindo(a) ao curso."


print(saudacao("Ana"))
print(saudacao("Carlos"))
print(saudacao("Mariana"))
