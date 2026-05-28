from typing import TypeVar, List, Callable

T = TypeVar('T')
R = TypeVar('R')

def aplicar_transformacao(dados: List[T], funcao: Callable[[T], R]) -> List[R]:
    """
    Aplica uma função de transformação a cada elemento de uma lista.

    Args:
        dados (List[T]): Lista de dados de entrada.
        funcao (Callable[[T], R]): Função de transformação.

    Returns:
        List[R]: Lista com os elementos transformados.
    """
    return [funcao(item) for item in dados]

# 1. Lista de strings → maiúsculas
strings = ["ola", "mundo", "python"]
print("Strings maiúsculas:", aplicar_transformacao(strings, lambda s: s.upper()))

# 2. Lista de floats → arredondados com 2 casas
floats = [3.14159, 2.71828, 1.61803]
print("Floats arredondados:", aplicar_transformacao(floats, lambda f: round(f, 2)))

# 3. Lista de dicionários → extraindo um campo específico
dicts = [{"id": 1, "nome": "Ana"}, {"id": 2, "nome": "Carlos"}]
print("Nomes extraídos:", aplicar_transformacao(dicts, lambda d: d["nome"]))
