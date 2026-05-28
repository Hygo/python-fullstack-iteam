from typing import TypeVar, List, Callable

T = TypeVar("T")
R = TypeVar("R")


def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """Aplica uma função de transformação a cada elemento da lista.

    Args:
        dados: Lista de elementos do tipo T a transformar.
        funcao: Função que converte T em R.

    Returns:
        Nova lista com os elementos transformados para o tipo R.

    Example:
        >>> aplicar_transformacao(["hello"], str.upper)
        ['HELLO']
    """
    return [funcao(item) for item in dados]


# 1. Strings → maiúsculas
palavras = ["python", "django", "postgresql"]
maiusculas = aplicar_transformacao(palavras, str.upper)
print("1. Strings em maiúsculas:")
print(f"   {maiusculas}")

# 2. Floats → arredondados com 2 casas
valores = [3.14159, 2.71828, 1.41421, 9.80665]
arredondados = aplicar_transformacao(valores, lambda x: round(x, 2))
print("\n2. Floats arredondados:")
print(f"   {arredondados}")

# 3. Dicionários → extraindo campo "nome"
usuarios = [
    {"nome": "Alefe",   "cargo": "Estudante"},
    {"nome": "Amanda", "cargo": "Estudante"},
    {"nome": "Luciano",    "cargo": "Estudante"},
]
nomes = aplicar_transformacao(usuarios, lambda u: u["nome"])
print("\n3. Nomes extraídos dos dicionários:")
print(f"   {nomes}")