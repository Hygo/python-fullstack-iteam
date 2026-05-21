from typing import TypeVar, List, Callable

T = TypeVar('T')  # Tipo de entrada
R = TypeVar('R')  # Tipo de saída

def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """
    Aplica uma função de transformação a cada elemento de uma lista.

    Args:
        dados (List[T]): Lista de elementos de tipo genérico T.
        funcao (Callable[[T], R]): Função que recebe um elemento T e retorna R.

    Returns:
        List[R]: Lista de elementos transformados do tipo R.

    Example:
        >>> aplicar_transformacao([1, 2, 3], lambda x: x * 2)
        [2, 4, 6]
    """
    return [funcao(item) for item in dados]


# --- Demonstração ---

# 1. Lista de strings → confidenciais (ex: mascarar nomes)
nomes = ["Alice", "Bruno", "Carla"]
nomes_confidenciais = aplicar_transformacao(nomes, lambda x: "***")
print("Strings confidenciais:", nomes_confidenciais)

# 2. Lista de números (carros alegóricos) → arredondados com 2 casas decimais
valores = [1234.5678, 9876.54321, 456.789]
valores_arredondados = aplicar_transformacao(valores, lambda x: round(x, 2))
print("Valores arredondados:", valores_arredondados)

# 3. Lista de dicionários → extraindo um campo específico (ex: 'nome')
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "Fernanda", "idade": 28}
]
nomes_extraidos = aplicar_transformacao(pessoas, lambda p: p["nome"])
print("Nomes extraídos:", nomes_extraidos)
