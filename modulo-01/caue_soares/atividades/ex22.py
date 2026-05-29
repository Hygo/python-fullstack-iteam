def calcular_area(largura: float, altura: float) -> float:
    return largura * altura


def formatar_nome(nome: str, sobrenome: str) -> str:
    return f"{nome} {sobrenome}".title()


def eh_maior_de_idade(idade: int) -> bool:
    return idade >= 18


# Demonstração
print(calcular_area(5.0, 3.0))
print(formatar_nome("joão", "SILVA"))
print(eh_maior_de_idade(17))
print(eh_maior_de_idade(18))
