"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Paulo Roberto de Souza Mesquita Junior
Data    : 20/05/2026
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
    temp = float(input("Digite a temperatura em Celsius: "))
    if temp < 0:
        print("❄️ Congelante")
    elif temp <= 14:
        print("🥶 Frio")
    elif temp <= 24:
        print("😊 Agradável")
    elif temp <= 34:
        print("☀️ Quente")
    else:
        print("🔥 Muito quente")


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
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if usuario == "admin" and senha == "iteam2025":
        print("Acesso concedido")
    else:
        print("Acesso negado")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    num = int(input("Digite um número para tabuada: "))
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")


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
    num = int(input("Digite um número para contagem regressiva: "))
    while num > 0:
        print(num, end=" ")
        num -= 1
    print("🚀 Lançamento!")


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
    for i, item in enumerate(estoque):
        if item == "Monitor":
            print(f"Monitor encontrado na posição {i}")
            break


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
    soma = 0
    total = 0
    # SUA SOLUÇÃO AQUI
    for leitura in leituras:
        if leitura is None:
            continue
        soma += leitura
        total += 1
    media = soma / total
    print(f"Soma: {soma}")
    print(f"Média: {media}")
    print(f"Total ignorado: {total}")


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
    while True:
        nota = float(input("Digite a nota do aluno: "))
        if 0 <= nota <= 10:
            break
    if nota >= 9:
        print("A – Excelente")
    elif nota >= 7:
        print("B – Bom")
    elif nota >= 5:
        print("C – Regular")
    else:
        print("D – Insuficiente")


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
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            print("Operação inválida")
    except ValueError:
        print("Valor inválido")
    except ZeroDivisionError:
        print("Divisão por zero")
    else:
        print("Resultado: ", resultado)
    finally:
        print("Fim do programa")


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
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for i in range(4, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


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
    for i in range(7):
        num = int(input("Digite um número: "))
        if num == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif num < numero_secreto:
            print("O número é maior")
        else:
            print("O número é menor")


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
    import math
    num = int(input("Digite um número: "))
    if num <= 1:
        print("Não é primo")
    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                print("Não é primo")
                break
        else:
            print("É primo")


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
    senha = input("Digite a senha: ")
    if len(senha) < 8:
        print("❌ Senha muito curta")
    if not any(c.isupper() for c in senha):
        print("❌ Senha sem letra maiúscula")
    if not any(c.islower() for c in senha):
        print("❌ Senha sem letra minúscula")
    if not any(c.isdigit() for c in senha):
        print("❌ Senha sem número")
    if not any(c in "!@#$%^&*" for c in senha):
        print("❌ Senha sem caractere especial")
    else:
        print("✅ Senha forte")


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
    valor = int(input("Digite o valor do saque: "))
    if valor % 10 != 0:
        print("O valor deve ser múltiplo de 10")
    if valor > 3000:
        print("O valor excede o limite de 3000")
    for cedula in cedulas:
        qtd = valor // cedula
        if qtd > 0:
            print(f"{qtd} cédulas de {cedula}")
            valor %= cedula


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
    while True:
        nota = input("Digite a nota do aluno: ")
        if nota == "fim":
            break
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida")
        except ValueError:
            print("Valor inválido")
    print(f"Total: {len(notas)}")
    print(f"Média: {sum(notas) / len(notas)}")
    print(f"Maior nota: {max(notas)}")
    print(f"Menor nota: {min(notas)}")


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
        opcao = input("Digite a opção: ")
        if opcao == "1":
            ex01_classificador_temperatura()
        elif opcao == "2":
            ex02_validador_acesso()
        elif opcao == "3":
            ex03_tabuada()
        elif opcao == "4":
            ex04_contador_regressivo()
        elif opcao == "5":
            ex05_buscador_break()
        elif opcao == "6":
            ex06_filtro_continue()
        elif opcao == "7":
            ex07_validacao_nota()
        elif opcao == "8":
            ex08_calculadora_segura()
        elif opcao == "9":
            ex09_padrao_numerico()
        elif opcao == "10":
            ex10_jogo_adivinhacao()
        elif opcao == "11":
            ex11_numero_primo()
        elif opcao == "12":
            ex12_analisador_senha()
        elif opcao == "13":
            ex13_caixa_eletronico()
        elif opcao == "14":
            ex14_leitura_notas_turma()
        elif opcao == "0":
            break
        else:
            print("Opção inválida")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Paulo Mesquita")
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
