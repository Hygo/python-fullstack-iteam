# Atividade 1 - Calculadora de Operações
#Alunos: Leticia Alves e Rafael Nobrega de Lima

# Contexto: calculadora aritmética com 6 operações. Conceito central: dicionário simples + lambdas como valores.
import math

# Registry
calculadora_operacoes = {}

def calcular_depois(nome:str):
    def decorator(classe):
        calculadora_operacoes[nome] = classe
        return classe
    return decorator

# ---------------- OPERAÇÕES ---------------- #
@calcular_depois("soma")
class Soma:
    def executar(self, a,b):
        return a + b
    
@calcular_depois("subtracao")
class Subtracao:
    def executar(self, a,b):
        return a - b
    
@calcular_depois("divisao")
class Divisao:
    def executar(self, a,b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ValueError("Não é possível dividir por zero")
    
@calcular_depois("multiplicacao")
class Multiplicacao:
    def executar(self, a,b):
        return a * b
    
@calcular_depois("potenciacao")
class Potenciacao:
    def executar(self, a,b):
        return a ** b
    
@calcular_depois("raiz")
class Radiciacao:
    def executar(self, a, b=None):

        if a < 0:
            raise ValueError("Não existe raiz real de número negativo")

        return math.sqrt(a)


# ---------------- CALCULADORA ---------------- #
def calcular(operacao: str, a: float, b: float = None):
    if operacao not in calculadora_operacoes:
        return f"Operação {operacao} inválida!!"
    
    classe_op = calculadora_operacoes[operacao]()
    return classe_op.executar(a,b)

# ---------------- TESTES ---------------- #

print(calcular("soma", 10, 10))
print(calcular("subtracao", 10, 3))
print(calcular("multiplicacao", 9, 3))
print(calcular("potenciacao", 2, 3))
print(calcular("raiz", 25))

# print(calcular("divisao", 10, 0))