def calcular_area(largura: float, altura: float) -> float:
    return largura * altura

def formatar_nome(nome: str, sobrenome: str) -> str:
    return f"{nome} {sobrenome}".title()

def eh_maior_de_idade(idade: int) -> bool:
    return idade >= 18