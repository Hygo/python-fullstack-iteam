"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Letícia Alves dos Santos
Data    : 21/05/2026
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
    elif 0 <= temp <= 14:
        print("🥶 Frio")
    elif 15 <= temp <= 24:
        print("😊 Agradável") 
    elif 25 <= temp <= 34:
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

    if usuario == "admin":
        if senha == "iteam2025":
            print("Acesso concedido!")
        else:
            print("Senha incorreta. Acesso negado.")
    else:
        print("Usuário não encontrado. Acesso negado.") 


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    num = input("Digite um número inteiro para ver sua tabuada: ")
    for i in range(1, 11):
        resultado = int(num) * i
        print(f"{num} x {i:2} = {resultado}")
        

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
    num = int(input("Digite um número inteiro positivo para a contagem regressiva: "))
    while num >= 0:
        print(num, end=" \n")
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

    # SUA SOLUÇÃO AQUI
    soma = 0
    ignorados = 0

    for leitura in leituras:
        if leitura == None:
            ignorados += 1
            continue

        soma += leitura

    media = soma / (len(leituras) - ignorados)

    print(f'A soma é: {soma}')
    print(f'A media é: {media}')
    print(f'Foram ignorados {ignorados} valores None')


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
    nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
    
    if 0.0 <= nota <= 10.0:
        if nota >= 9.0:
            print("A – Excelente")
        elif nota >= 7.0:
            print("B – Bom")
        elif nota >= 5.0:
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
        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        op = input("Operação: ")

        if op == "+":
            r = n1 + n2

        elif op == "-":
            r = n1 - n2

        elif op == "*":
            r = n1 * n2

        elif op == "/":
            r = n1 / n2

        else:
            print("Operação inválida")

    except:
        print("Erro")

    else:
        print(r)

    finally:
        print("Fim")


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
    tentativas = 7
    while tentativas > 0:
        tentativa = int(input("Digite um número entre 1 e 100: "))
        if tentativa == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif tentativa < numero_secreto:
            print("O número é maior.")
        else:
            print("O número é menor.")
        tentativas -= 1
    if tentativas == 0:
        print(f"Suas tentativas acabaram. O número era {numero_secreto}.")


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
    try:
        entrada = input("Digite um número inteiro positivo: ")
        n = int(entrada)
        
        # Se for menor ou igual a zero, dispara o ValueError de propósito
        if n <= 0:
            raise ValueError("O número deve ser positivo (maior que zero).")
            
        if n == 1:
            print("O número 1 não é primo.")
            return
            
        eh_primo = True
        
        for i in range(2, n):
            if n % i == 0:
                eh_primo = False
                print(f"Encontrou o divisor {i}. Interrompendo a busca com 'break'...")
                break
        
        if eh_primo:
            print(f"O número {n} é PRIMO!")
        else:
            print(f"O número {n} NÃO é primo.")

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros e positivos (maiores que zero).")


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
    senha = input("Digite a senha para análise: ")
    
    comprimento_ok = len(senha) >= 8
    maiuscula_ok = False
    minuscula_ok = False
    digito_ok = False
    especial_ok = False
    
    especiais = "!@#$%^&*"
   
    for letra in senha:
        if letra.isupper():
            maiuscula_ok = True
        if letra.islower():
            minuscula_ok = True
        if letra.isdigit():
            digito_ok = True
        if letra in especiais:
            especial_ok = True

    emoji_tamanho = "❌"
    emoji_maiuscula = "❌"
    emoji_minuscula = "❌"
    emoji_digito = "❌"
    emoji_especial = "❌"
    
    if comprimento_ok:
        emoji_tamanho = "✅"
    if maiuscula_ok:
        emoji_maiuscula = "✅"
    if minuscula_ok:
        emoji_minuscula = "✅"
    if digito_ok:
        emoji_digito = "✅"
    if especial_ok:
        emoji_especial = "✅"

    print("\n=== RELATÓRIO DA SENHA ===")
    print(f"{emoji_tamanho} Mínimo 8 caracteres")
    print(f"{emoji_maiuscula} Pelo menos 1 maiúscula")
    print(f"{emoji_minuscula} Pelo menos 1 minúscula")
    print(f"{emoji_digito} Pelo menos 1 dígito")
    print(f"{emoji_especial} Pelo menos 1 caractere especial")
    print("==========================")
    
    if comprimento_ok and maiuscula_ok and minuscula_ok and digito_ok and especial_ok:
        print("Resultado: Senha FORTE! 💪")
    
    if not (comprimento_ok and maiuscula_ok and minuscula_ok and digito_ok and especial_ok):
        print("Resultado: Senha FRACA! ❌")
    

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
    while True:
        try:
            valor = int(input("Digite o valor do saque: R$"))

            if valor <= 0:
                print("Digite um valor maior que zero.")
            elif valor > 3000:
                print("Valor máximo permitido: R$3000.")
            elif valor % 10 != 0:
                print("O valor deve ser múltiplo de R$10.")
            else:
                print("\nCédulas entregues:")

                for cedula in cedulas:
                    qtd = valor // cedula
                    if qtd > 0:
                        print(f"{qtd} cédula(s) de R${cedula}")
                    valor %= cedula
                break
            
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

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
        entrada = input("Digite uma nota (ou 'fim'): ")

        if entrada.lower() == "fim":
            break
        try:
            nota = float(entrada)

            if nota < 0 or nota > 10:
                print("Nota inválida. Digite entre 0 e 10.")
                continue
            notas.append(nota)

        except ValueError:
            print("Entrada inválida.")
            pass
            continue

    if len(notas) > 0:
        total = len(notas)
        media = sum(notas) / total
        maior = max(notas)
        menor = min(notas)

        print("\nResultado:")
        print(f"Total de notas: {total}")
        print(f"Média: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")

    else:
        print("Nenhuma nota foi informada.")


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
        try:
            opcao = int(input("Escolha uma opção: "))

            # Sair
            if opcao == 0:
                print("Saindo do sistema...")
                break

            # Opção 1
            elif opcao == 1:
                celsius = float(input("Digite a temperatura em Celsius: "))

                fahrenheit = (celsius * 9/5) + 32

                print(f"A temperatura de {celsius}°C corresponde a {fahrenheit:.2f}°F")

            # Opção 2
            elif opcao == 2:
                numero = int(input("Digite um número: "))

                if numero < 2:
                    print("Não é primo.")

                else:
                    primo = True

                    for i in range(2, numero):

                        if numero % i == 0:
                            primo = False
                            break

                    if primo:
                        print("Número primo.")
                    else:
                        print("Não é primo.")

            # Opção 3
            elif opcao == 3:
                senha = input("Digite a senha: ")

                tem_numero = False

                for caractere in senha:
                    if caractere.isdigit():
                        tem_numero = True

                print(f"Tamanho: {len(senha)}")

                if len(senha) >= 8:
                    print("Comprimento válido")
                else:
                    print("Senha curta")

                if tem_numero:
                    print("Possui dígito")
                else:
                    print("Não possui dígito")

            # Opção 4
            elif opcao == 4:

                n1 = float(input("Primeiro número: "))
                operador = input("Operador (+ - * /): ")
                n2 = float(input("Segundo número: "))

                if operador == "+":
                    print("Resultado:", n1 + n2)

                elif operador == "-":
                    print("Resultado:", n1 - n2)

                elif operador == "*":
                    print("Resultado:", n1 * n2)

                elif operador == "/":

                    if n2 == 0:
                        print("Não é possível dividir por zero")
                        continue

                    print("Resultado:", n1 / n2)

                else:
                    print("Operador inválido")

            else:
                print("Opção inválida")

        except ValueError:
            print("Entrada inválida. Digite valores corretos.")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Letícia Alves dos Santos")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    #ex01_classificador_temperatura()
    #ex02_validador_acesso()
    #ex03_tabuada()
    #ex04_contador_regressivo()
    # ex05_buscador_break()
    #ex06_filtro_continue()
    #ex07_validacao_nota()
    #ex08_calculadora_segura()
    #ex09_padrao_numerico()
    #ex10_jogo_adivinhacao()
    #ex11_numero_primo()
    #ex12_analisador_senha()
    #ex13_caixa_eletronico()
    #ex14_leitura_notas_turma()
    #ex15_menu_sistema()
