"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Leonam De Sousa Silva
Data    : 22/06/2026
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
    try:
        temp = float(input("Digite a temperatura em °C: "))
        
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
    except ValueError:
        print("Erro: Digite um valor numérico válido.")


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
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin":
        if senha == "iteam2025":
            print(" Acesso concedido! Bem-vindo ao sistema.")
        else:
            print(" Falha no acesso: Senha incorreta.")
    else:
        print(" Falha no acesso: Usuário não cadastrado.")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    try:
        num = int(input("Digite um número inteiro para ver a tabuada: "))
        print(f"\n--- Tabuada do {num} ---")
        for i in range(1, 11):
            resultado = num * i
            print(f"{num} x {i:>2} = {resultado:>3}")
    except ValueError:
        print("Erro: Forneça um número inteiro válido.")


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    try:
        contador = int(input("Digite um número inteiro positivo para a contagem: "))
        if contador < 0:
            print("Por favor, digite um número positivo.")
            return

        print("Iniciando contagem: ", end="")
        while contador >= 0:
            print(contador, end="... " if contador > 0 else " ")
            contador -= 1
        print(" Lançamento!")
    except ValueError:
        print("Erro: Forneça um número inteiro válido.")


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

    encontrado = False
    for indice, item in enumerate(estoque):
        if item == "Monitor":
            print(f"Item 'Monitor' localizado com sucesso no índice {indice}.")
            encontrado = True
            break
            
    if not encontrado:
        print("Item não encontrado no estoque.")


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

    soma = 0.0
    validos = 0
    ignorados = 0

    for leitura in leituras:
        if leitura is None:
            ignorados += 1
            continue
        soma += leitura
        validos += 1

    media = soma / validos if validos > 0 else 0

    print(f"Soma das leituras válidas : {soma:.2f}")
    print(f"Média das leituras válidas: {media:.2f}")
    print(f"Registros nulos ignorados : {ignorados}")


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
    while True:
        try:
            nota = float(input("Digite uma nota entre 0.0 e 10.0: "))
            if 0.0 <= nota <= 10.0:
                break
            print("Nota inválida! O valor deve estar estritamente entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida! Digite um número real.")

    if nota >= 9.0:
        conceito = "A – Excelente"
    elif nota >= 7.0:
        conceito = "B – Bom"
    elif nota >= 5.0:
        conceito = "C – Regular"
    else:
        conceito = "D – Insuficiente"

    print(f"Conceito final do aluno: {conceito}")


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
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ").strip()

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            raise ValueError("Operação inválida.")
            
    except ValueError as e:
        if str(e) == "Operação inválida.":
            print("Erro: Operador matemático não reconhecido.")
        else:
            print("Erro: Entrada de dados inválida. Digite valores numéricos.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida na matemática.")
    else:
        print(f"Sucesso! O resultado de ({num1} {operacao} {num2}) = {resultado}")
    finally:
        print("Processamento da calculadora concluído.")


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
    print("--- Triângulo Crescente ---")
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print("\n--- Desafio Extra: Decrescente ---")
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
    tentativas_restantes = 7

    print("🤖 Pensei em um número de 1 a 100. Você consegue adivinhar em 7 tentativas?")

    while tentativas_restantes > 0:
        try:
            palpite = int(input(f"\n[{tentativas_restantes} tent.] Seu palpite: "))
            
            if palpite == numero_secreto:
                print(f"🏆 Parabéns! Você acertou. O número era mesmo {numero_secreto}!")
                return
            elif palpite < numero_secreto:
                print(" Errou! O número secreto é MAIOR.")
            else:
                print(" Errou! O número secreto é MENOR.")
                
            tentativas_restantes -= 1
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    print(f"\n💥 Game Over! Suas chances acabaram. O número era {numero_secreto}.")


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
    import math
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n <= 1:
            print(f"O número {n} não é considerado primo.")
            return

        eh_primo = True
        limite = int(math.isqrt(n)) # Otimização matemática usando a raiz quadrada inteira

        for i in range(2, limite + 1):
            if n % i == 0:
                eh_primo = False
                break

        if eh_primo:
            print(f" {n} é um número primo!")
        else:
            print(f"Recusado{n} NÃO é um número primo (divisível por {i}).")
            
    except ValueError:
        print("Erro: Forneça uma entrada numérica inteira válida.")


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
    senha = input("Digite a senha para análise: ")
    especiais = "!@#$%^&*"

    # Flags de verificação
    c_tamanho = len(senha) >= 8
    c_maiuscula = False
    c_minuscula = False
    c_digito = False
    c_especial = False

    for char in senha:
        if char.isupper():
            c_maiuscula = True
        elif char.islower():
            c_minuscula = True
        elif char.isdigit():
            c_digito = True
        elif char in especiais:
            c_especial = True

    print("\n=== RELATÓRIO DE SEGURANÇA ===")
    print(f"{'aceito' if c_tamanho else 'Recusado'} Mínimo de 8 caracteres")
    print(f"{'aceito' if c_maiuscula else 'Recusado'} Pelo menos 1 letra maiúscula")
    print(f"{'aceito' if c_minuscula else 'Recusado'} Pelo menos 1 letra minúscula")
    print(f"{'aceito' if c_digito else 'Recusado'} Pelo menos 1 dígito numérico")
    print(f"{'aceito' if c_especial else 'Recusado'} Pelo menos 1 caractere especial (!@#$%^&*)")
    print("==============================")

    if c_tamanho and c_maiuscula and c_minuscula and c_digito and c_especial:
        print(" Status: SENHA FORTE")
    else:
        print(" Status: SENHA FRACA. Corrija os pontos marcados com Recusado.")


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
    
    try:
        valor = int(input("Digite o valor para saque (Múltiplos de R$10 até R$3000): R$ "))
        
        if valor < 10 or valor > 3000:
            print("Operação Recusada: Valor fora do limite operacional (R$10 a R$3.000).")
            return
        if valor % 10 != 0:
            print("Operação Recusada: Este caixa disponibiliza apenas notas de R$10, R$20, R$50, R$100 e R$200.")
            return

        print("\nDispensando cédulas:")
        valor_restante = valor
        
        for cedula in cedulas:
            qtd_cedulas = valor_restante // cedula
            if qtd_cedulas > 0:
                print(f" - {qtd_cedulas} cédula(s) de R$ {cedula}")
                valor_restante %= cedula
                
    except ValueError:
        print("Erro: Digite um valor numérico inteiro.")


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

    while True:
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ").strip().lower()
        
        if entrada == "fim":
            break
            
        try:
            nota = float(entrada)
            if not (0.0 <= nota <= 10.0):
                print(" Aviso: Nota fora da escala permitida (0.0 a 10.0). Ignorada.")
                continue
            notas.append(nota)
        except ValueError:
            print(" Entrada inválida. Digite uma nota numérica válida ou a palavra 'fim'.")
            continue

    if not notas:
        print("Nenhuma nota válida foi registrada no sistema.")
        return

    print("\n=== ESTATÍSTICAS DA TURMA ===")
    print(f"Quantidade de notas: {len(notas)}")
    print(f"Média aritmética   : {sum(notas) / len(notas):.2f}")
    print(f"Maior nota obtida  : {max(notas):.1f}")
    print(f"Menor nota obtida  : {min(notas):.1f}")


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

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: Digite apenas os números correspondentes às opções do menu.")
            continue

        if opcao == 0:
            print("Encerrando o Sistema ITEAM. Até logo!")
            break

        elif opcao == 1:
            print("\n[Subsistema] Conversor de Temperatura")
            try:
                celsius = float(input("Digite em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"Resultado: {celsius}°C = {fahrenheit:.1f}°F")
            except ValueError:
                print("Erro: Valor numérico inválido.")

        elif opcao == 2:
            print("\n[Subsistema] Verificador de Número Primo")
            try:
                n = int(input("Digite um número inteiro: "))
                if n <= 1:
                    print("Não é primo.")
                else:
                    primo = True
                    for i in range(2, n):
                        if n % i == 0:
                            primo = False
                            break
                    print(f"Resultado: {'É Primo' if primo else 'Não é Primo'}")
            except ValueError:
                print("Erro: Entrada inválida.")

        elif opcao == 3:
            print("\n[Subsistema] Analisador de Senha Simples")
            senha = input("Digite a senha: ")
            tem_digito = any(char.isdigit() for char in senha)
            tam_valido = len(senha) >= 6
            
            if tam_valido and tem_digito:
                print("🔒 Senha aceitável (Mínimo de 6 caracteres e possui número).")
            else:
                print("Recusado Senha rejeitada. Deve ter pelo menos 6 caracteres e conter 1 dígito.")

        elif opcao == 4:
            print("\n[Subsistema] Calculadora Básica Segura")
            try:
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                op = input("Operação (+, -, *, /): ").strip()
                if op == "+": print(f"Resultado: {n1 + n2}")
                elif op == "-": print(f"Resultado: {n1 - n2}")
                elif op == "*": print(f"Resultado: {n1 * n2}")
                elif op == "/": print(f"Resultado: {n1 / n2}")
                else: print("Operação Inválida.")
            except ZeroDivisionError:
                print("Erro: Divisão por zero.")
            except ValueError:
                print("Erro: Valor numérico inválido.")
        else:
            print("Opção inválida! Escolha um número presente no menu.")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Leonam De Sousa Silva")
    print("=" * 50)

    # Descomente linha por linha conforme for testando:
    # ex01_classificador_temperatura()
    # ex02_validador_acesso()
    # ex03_tabuada()
    # ex04_contador_regressivo()
    # ex05_buscador_break()
    # ex06_filtro_continue()
    # ex07_validacao_nota()
    # ex08_calculadora_segura()
    # ex09_padrao_numerico()
    # ex10_jogo_adivinhacao()
    # ex11_numero_primo()
    # ex12_analisador_senha()
    # ex13_caixa_eletronico()
    # ex14_leitura_notas_turma()
    # ex15_menu_sistema()