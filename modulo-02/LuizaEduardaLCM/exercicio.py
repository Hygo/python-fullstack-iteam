"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <LUIZA EDUARDA LOPES DA CONCEICAO MENDES>
Data    : <22/05/2026>
=============================================================

INSTRUÇÕES:
  1. Substitua <SEU NOME COMPLETO AQUI> e <DATA DE ENTREGA> acima.
  2. Implemente cada função no espaço indicado com # SUA SOLUÇÃO AQUI.
  3. Não apague os comentários de orientação.
  4. Execute o arquivo para testar suas soluções antes de enviar.
  5. Suba este arquivo na pasta:
       alunos/<seu_nome>/modulo-02/exercicios.py

COMO EXECUTAR:
  python exercicios.py
=============================================================
"""


# ==============================================================
# EXERCÍCIO 01 – Classificador de Temperatura
# Conceitos: if / elif / else, float(), input()
# ==============================================================
def ex01_classificador_temperatura():
    """
    Lê uma temperatura em Celsius e exibe sua classificação.

    Faixas:
        < 0        → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
temperatura = float(input("Qual a temperatura de hoje? "))

if temperatura < 0:
    print("Hoje está ❄️ Congelante")

elif 0 <= temperatura <= 14:
    print("Hoje está 🥶 Frio")

elif 15 <= temperatura <= 24:
    print("Hoje está 😊 Agradável")

elif 25 <= temperatura <= 34:
    print("Hoje está ☀️ Quente")

else:
    print("Hoje está 🔥 Muito quente")
"""

# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2025"
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
usuario = input("Digite seu usuário: ")
if usuario == "admin":
    senha = input("Digite sua senha: ")

    if senha == "iteam2025":
        print("Acesso liberado! Bem-vindo, admin.")

    else:
        print("Senha incorreta. Acesso negado.")

else:
    print("Usuário não encontrado. Acesso negado.")
"""

# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
num = int(input("Digite um número: "))
print(f'Tabuada de {num}:')

for i in range(1, 11):
    resultado = num * i
    print(f'{num:2} x {i:2} = {resultado:3}')
"""

# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
num = int(input("Digite um número positivo para a contagem regressiva: "))
while num >= 0:
    print(num, end=" ")
    num -= 1
print("🚀 Lançamento!")
"""

# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    """
    Percorre o estoque e localiza 'Monitor', exibindo
    sua posição. Usa break ao encontrar o item.
    """
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    # SUA SOLUÇÃO AQUI
    pass

"""
estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]
encontrado = False

busca = input("Digite o item que deseja buscar no estoque: ")
for indice, item in enumerate(estoque):
    if item == busca:
        print(f'Item {busca} encontrado na posição {indice}.')
        encontrado = True
        break
    else:
        print(f'Item {busca} não encontrado no estoque.')
"""

# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    """
    Percorre a lista de leituras, ignora os valores None
    com continue e calcula soma, média e total ignorado.
    """
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    # SUA SOLUÇÃO AQUI
    pass
"""
leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]
soma = 0
contador = 0
total_ignorados = 0
for leitura in leituras:
    if leitura is None:
        total_ignorados += 1
        continue
    soma += leitura
    contador += 1
if contador > 0:
    media = soma / contador 
else:
    media = 0
print(f'Soma das leituras válidas: {soma:.2f}')
print(f'Média das leituras válidas: {media:.2f}')
print(f'Total de leituras ignoradas: {total_ignorados}')
"""

# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    """
    Solicita a nota do aluno repetidamente até receber
    um valor válido (0.0 a 10.0), então exibe o conceito.

    Conceitos:
        9.0 a 10.0 → A – Excelente
        7.0 a 8.9  → B – Bom
        5.0 a 6.9  → C – Regular
        < 5.0      → D – Insuficiente
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
while True:
    if 0.0 <= nota <= 10.0:
        if nota >= 9.0:
            conceito = "A"
            print(f'Nota do aluno: {nota:.1f} - A')
        elif nota >= 7.0:
            conceito = "B"
            print(f'Nota do aluno: {nota:.1f} - B')
        elif nota >= 5.0:
            conceito = "C"
            print(f'Nota do aluno: {nota:.1f} - C')
        else:
            conceito = "D"
            print(f'Nota do aluno: {nota:.1f} - D')
        break
    else:
        print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
"""

# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    # SUA SOLUÇÃO AQUI
    pass

"""
    try:
        num = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao not in ["+", "-", "*", "/"]:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")
        num2 = float(input("Digite o segundo número: "))
        if operacao == "+":
            resultado = num + num2
        elif operacao == "-":
            resultado = num - num2
        elif operacao == "*":
            resultado = num * num2
        elif operacao == "/":
            if num2 == 0:
                raise ZeroDivisionError("Divisão por zero não é permitida.")
            resultado = num / num2
    except ValueError as ve:
        print(f"Erro: {ve}")
    except ZeroDivisionError as zde:
        print(f"Erro: {zde}")
    else:
        print(f'O resultado de {num} {operacao} {num2} é: {resultado}')
    finally:
        print("Calculadora encerrada!")
"""
# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
for i in range(0, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("===========")

for i in range(6, 0, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
"""

# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """
    import random
    numero_secreto = random.randint(1, 100)

    # SUA SOLUÇÃO AQUI
    pass
"""
import random

numero_secreto = random.randint(1, 100)
tentativas = 7
print("Bem-vindo ao Jogo de Adivinhação!")
print(f"Eu escolhi um número entre 1 e 100. Você tem {tentativas} tentativas para adivinhar.")

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))
    if palpite < numero_secreto:
        print("O número é maior do que isso.")
    elif palpite > numero_secreto:
        print("O número é menor do que isso.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativa} tentativas!")
        break
else:
    print(f"💀 Game over! Suas tentativas acabaram, o número secreto era {numero_secreto}.")
"""

# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    """
    Solicita um número inteiro positivo e verifica se é primo.
    Usa break ao encontrar o primeiro divisor.
    Trata ValueError e números negativos/zero.
    Otimização: verifica divisores somente até √n.
    """
    # SUA SOLUÇÃO AQUI
    pass
"""
try:
    num = int(input("Digite um número inteiro positivo para verificar se é primo: "))
    
    if num <= 1:
        print("Números menores ou iguais a 1 não são primos.")
    else:
        primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                primo = False
                break 
        
        if primo:
            print(f"{num} é um número primo.")
        else:
            print(f"{num} não é um número primo.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro positivo.")
else:
    print("Verificação concluída.")
    """

# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Analisa se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    # SUA SOLUÇÃO AQUI
    pass

senha = "Python@2025"
senha = input("Digite uma senha para análise: ")
criterios = {
    "Tamanho mínimo (8 caracteres)": len(senha) >= 8,
    "Contém letra maiúscula": any(c.isupper() for c in senha),
    "Contém letra minúscula": any(c.islower() for c in senha),
    "Contém dígito": any(c.isdigit() for c in senha),
    "Contém caractere especial": any(c in "!@#$%^&*" for c in senha)
}

for critério, atendido in criterios.items():
    if not atendido:
        print(input("Tente novamente com uma senha mais forte: "))
        print(f'Critérios: {criterios}')
    else:
        print(f"   - A senha '{senha}' atende ao critério: {critério}")
        print("   - Ótimo! Senha criada.")
# ==============================================================
# EXERCÍCIO 13 – Simulador de Caixa Eletrônico
# Conceitos: while, //, if/else, try/except
# ==============================================================
def ex13_caixa_eletronico():
    """
    Solicita um valor de saque (múltiplo de R$10, máx R$3.000).
    Calcula o menor número de cédulas: R$200, R$100, R$50, R$20, R$10.
    Trata entradas inválidas.
    """
    cedulas = [200, 100, 50, 20, 10]

    # SUA SOLUÇÃO AQUI
    pass
"""
saque = int(input("Digite o valor do saque (múltiplo de R$10, máximo R$3.000): "))
if saque % 10 != 0 or saque > 3000 or saque <= 0:
    print("Valor inválido. O saque deve ser um múltiplo de R$10, maior que 0 e no máximo R$3.000.")
else:
    print(f"Valor do saque: R${saque}")
    for cedula in [200, 100, 50, 20, 10]:
        quantidade = saque // cedula
        if quantidade > 0:
            print(f"{quantidade} cédula(s) de R${cedula}")
            saque -= quantidade * cedula
        else:
            print(f"0 cédula(s) de R${cedula}")
"""
# ==============================================================
# EXERCÍCIO 14 – Leitura de Múltiplos Dados com Tratamento
# Conceitos: while, break, continue, try/except, pass
# ==============================================================
def ex14_leitura_notas_turma():
    """
    Lê notas de uma turma até o usuário digitar 'fim'.
    Ignora notas inválidas com continue + mensagem de aviso.
    Ao encerrar, exibe: total, média, maior e menor nota.
    """
    notas = []

    # SUA SOLUÇÃO AQUI
    pass
"""
nota = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
while nota.lower() != 'fim':
    try:
        valor = float(nota)
        if 0.0 <= valor <= 10.0:
            notas.append(valor)
        else:
            print("Nota inválida. Digite um valor entre 0.0 e 10.0.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim' para encerrar.")
    nota = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
if notas:
    total = len(notas)
    media = sum(notas) / total
    maior = max(notas)
    menor = min(notas)
    print(f"Total de notas: {total}")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
"""
# ==============================================================
# EXERCÍCIO 15 – Desafio Final: Menu de Sistema
# Conceitos: while True, if/elif/else, break, continue, try/except
# ==============================================================
def ex15_menu_sistema():
    """
    Menu interativo que permanece ativo até o usuário sair.

    Opções:
        [1] Conversor de temperatura (Celsius → Fahrenheit)
        [2] Verificador de número primo (versão simplificada)
        [3] Analisador de senha (apenas comprimento e dígito)
        [4] Calculadora segura (só +, -, *, /)
        [0] Sair

    Usa try/except em toda entrada do usuário.
    """
    """
    while True:
        print("\n" + "=" * 29)
        print("   SISTEMA ITEAM - MENU    ")
        print("=" * 29)
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")
        print("=" * 29)

        # SUA SOLUÇÃO AQUI — leia a opção e implemente cada funcionalidade
        pass
        """
"""
menu = input("Escolha uma opção: ")
try:
    opcao = int(menu)
    if opcao == 1:  
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F.")
    elif opcao == 2:
        num = int(input("Digite um número inteiro positivo para verificar se é primo: "))
        if num <= 1:
            print("Números menores ou iguais a 1 não são primos.")
        else:
            primo = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                print(f"{num} é um número primo.")
            else:
                print(f"{num} não é um número primo.")
    elif opcao == 3:
        senha = input("Digite uma senha para análise: ")
        criterios = {
            "Tamanho mínimo (8 caracteres)": len(senha) >= 8,
            "Contém dígito": any(c.isdigit() for c in senha)
        }
        for critério, atendido in criterios.items():
            status = "✅" if atendido else "❌"
            print(f"{status} {critério}")
    elif opcao == 4:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida. Use apenas +, -, * ou /.")
        else:
            num2 = float(input("Digite o segundo número: "))
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                else:
                    resultado = num1 / num2
                    print(f'O resultado de {num1} {operacao} {num2} é: {resultado}')
    elif opcao == 0:
        print("Saindo do sistema. Até logo!")
        return
    else:
        print("Opção inválida. Por favor, escolha uma opção do menu.")
except ValueError:
    print("Entrada inválida. Por favor, digite um número correspondente às opções do menu.")
"""
# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): <Luiza Eduarda Lopes da Conceição Mendes>")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    ex01_classificador_temperatura()
    ex02_validador_acesso()
    ex03_tabuada()
    ex04_contador_regressivo()
    ex05_buscador_break()
    ex06_filtro_continue()
    ex07_validacao_nota()
    ex08_calculadora_segura()
    ex09_padrao_numerico()
    ex10_jogo_adivinhacao()
    ex11_numero_primo()
    ex12_analisador_senha()
    ex13_caixa_eletronico()
    ex14_leitura_notas_turma()
    ex15_menu_sistema()
