# basket = {'apple', 'banana', 'orange', 'grape', 'apple'}
# s1={1,2,3} 
# s2={3,4,5}
# print('banana' in basket)  # True
# print(s1|s2) # {1, 2, 3, 4, 5}
# print(s1&s2) # {3}
# print(s1-s2) # {1, 2} 
# print(s2-s1) # {4, 5}

# def fatorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fatorial(n-1)
    
# print(fatorial(10))  # Output: 120


# def somar(a, b):
#     return a + b
# def subtrair(a, b):
#     return a - b
# def multiplicar(a, b):
#     return a * b
# def dividir(a, b):
#     return a / b

# def calcular(a, b, operacao):
#         if operacao == 'soma':
#             return somar(a, b)
#         elif operacao == 'subtracao':
#             return subtrair(a, b)
#         elif operacao == 'multiplicacao':
#             return multiplicar(a, b)
#         elif operacao == 'divisao':
#             return dividir(a, b)
#         else:
#             raise ValueError("Operação inválida")
# print(calcular(10, 5, 'soma'))  # Output: 15
# print(calcular(10, 5, 'subtracao'))  # Output: 5
# print(calcular(10, 5, 'multiplicacao'))  # Output: 50
# print(calcular(10, 5, 'divisao'))  # Output: 2.0

# notas = [7.5, 8.0, 6.0, 9.0, 5.5]

# def aprovado(notas):
#     return notas >=7 
# resultados = list(filter(aprovado, notas))
# set_notas = set(['ana', 'maria', 'joao'])
# print(resultados)  # Output: [7.5, 8.0, 9.0]

# import os, sys 

# print(os.getcwd())  # Imprime o diretório de trabalho atual
# print(sys.version)  # Imprime a versão do Python em uso

# python

# Definição da classe Pessoa

class Pessoa:

# Metodo construtor: inicializa os atributos ao criar mовресo
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    # idade

    # Atributo de instancia

    # Netodo que representa a comportamento do objeto
    def apresentar_se(self):

    #Retorna a string formatada com os dados do objeco
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

#Criando objetos (Instancias) a partir da classe

pessoa1 = Pessoa ("Ana", 28)  #instancia a classe con argimentas

pessoa2 = Pessoa ("Carlos", 35)  #Outra instância independente



# Chando a sétodo para nahit a apresentação
print(pessoa1.apresentar_se()) # Saida: Olá, neu nome è Ana e tenho 26 anos.
print(pessoa2.apresentar_se()) # Sarda, ola, seu nome é Carlos e tenho 35 anos.