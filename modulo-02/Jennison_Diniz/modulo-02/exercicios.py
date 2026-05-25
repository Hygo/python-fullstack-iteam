"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Jennison Enthony Oliveira Diniz
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
    temperatura = float(input("Digite a temperatura em Celsius: "))
    if temperatura < 0:
        print("❄️ Congelante")
    elif temperatura <= 14:
        print("🥶 Frio")
    elif temperatura <= 24:
        print("😊 Agradável")
    elif temperatura <= 34:
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
        senha   → "123456"
    """
    # SUA SOLUÇÃO AQUI
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if usuario == "admin":
        if senha == "123456":
            print("Acesso concedido! Bem-vindo.")
        else:
            print("Falha no acesso: Senha incorreta.")
    else:
        print("Falha no acesso: Usuário inexistente.")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    numero = int(input("Digite um número para ver sua tabuada: "))
    print(f"\n--- Tabuada do {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado:2}")


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
    numero = int(input("Digite um número inteiro positivo para a contagem: "))
    while numero >= 0:
        print(numero, end=" ")
        numero -= 1
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
    for indice, item in enumerate(estoque):
        if item == "Monitor":
            print(f"Item 'Monitor' encontrado na posição {indice}!")
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
    contagem_validos = 0
    contagem_ignorados = 0

    for leitura in leituras:
        if leitura is None:
            contagem_ignorados += 1
            continue
        soma += leitura
        contagem_validos += 1

    media = soma / contagem_validos if contagem_validos > 0 else 0

    print(f"Soma das leituras válidas: {soma:.2f}")
    print(f"Média das leituras válidas: {media:.2f}")
    print(f"Total de registros ignorados (None): {contagem_ignorados}")


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
        try:
            nota = float(input("Digite uma nota entre 0.0 e 10.0: "))
            if 0.0 <= nota <= 10.0:
                break
            else:
                print("Nota fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número decimal válido.")

    if nota >= 9.0:
        print("Conceito: A – Excelente")
    elif nota >= 7.0:
        print("Conceito: B – Bom")
    elif nota >= 5.0:
        print("Conceito: C – Regular")
    else:
        print("Conceito: D – Insuficiente")


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
            raise ValueError("Operação inválida!")

    except ValueError as e:
        if "Operação inválida!" in str(e):
            print("Erro: Operação matemática não reconhecida.")
        else:
            print("Erro: Entrada inválida. Digite números válidos.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(f"Resultado da operação: {resultado}")
    finally:
        print("Processamento da calculadora finalizado.")


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
    # Triângulo crescente
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    # Triângulo decrescente (Desafio Extra)
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
    tentativas = 7
    ganhou = False

    print("--- JOGO DE ADIVINHAÇÃO ---")
    print("Pensei em um número entre 1 e 100. Você tem 7 tentativas para adivinhar!")

    while tentativas > 0:
        try:
            palpite = int(input(f"\nTentativas restantes: {tentativas}. Seu palpite: "))
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
            continue

        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou! O número secreto era {numero_secreto}.")
            ganhou = True
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")

        tentativas -= 1

    if not ganhou:
        print(f"\n💥 Que pena, suas tentativas acabaram! O número secreto era {numero_secreto}.")


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
        num = int(input("Digite um número inteiro positivo: "))
        if num <= 0:
            print("Erro: O número deve ser estritamente positivo.")
            return
        
        if num == 1:
            print("O número 1 não é primo.")
            return

        primo = True
        # Limite otimizado: parte inteira de da raiz quadrada de num
        limite = int(num ** 0.5)

        for i in range(2, limite + 1):
            if num % i == 0:
                primo = False
                break

        if primo:
            print(f"O número {num} é PRIMO. ✅")
        else:
            print(f"O número {num} NÃO É PRIMO. ❌")

    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
    """
    Análise se uma senha atende aos critérios de segurança:
        - Mínimo 8 caracteres
        - Pelo menos 1 maiúscula
        - Pelo menos 1 minúscula
        - Pelo menos 1 dígito
        - Pelo menos 1 caractere especial: !@#$%^&*

    Exibe relatório com ✅ ou ❌ para cada critério.
    """
    # SUA SOLUÇÃO AQUI
    senha = input("Digite a senha para análise: ")
    
    caracteres_especiais = "!@#$%^&*"
    
    c_comprimento = len(senha) >= 8
    c_maiuscula = False
    c_minuscula = False
    c_digito = False
    c_especial = False

    for char in senha:
        if char.isupper():
            c_maiuscula = True
        if char.islower():
            c_minuscula = True
        if char.isdigit():
            c_digito = True
        if char in caracteres_especiais:
            c_especial = True

    print("\n--- RELATÓRIO DE SEGURANÇA DA SENHA ---")
    print(f"{'✅' if c_comprimento else '❌'} Mínimo 8 caracteres")
    print(f"{'✅' if c_maiuscula else '❌'} Pelo menos 1 maiúscula")
    print(f"{'✅' if c_minuscula else '❌'} Pelo menos 1 minúscula")
    print(f"{'✅' if c_digito else '❌'} Pelo menos 1 dígito")
    print(f"{'✅' if c_especial else '❌'} Pelo menos 1 caractere especial (!@#$%^&*)")

    if c_comprimento and c_maiuscula and c_minuscula and c_digito and c_especial:
        print("\nResultado: Senha FORTE! 💪")
    else:
        print("\nResultado: Senha FRACA! ⚠️")


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
    try:
        valor = int(input("Digite o valor para saque (Múltiplos de R$10 até R$3000): R$ "))
        
        if valor <= 0 or valor > 3000:
            print("Erro: Valor de saque inválido. O limite é de R$ 10 a R$ 3000.")
            return
        if valor % 10 != 0:
            print("Erro: Valor indisponível. Este caixa possui apenas cédulas de R$200, R$100, R$50, R$20 e R$10.")
            return

        print(f"\nRealizando saque de R$ {valor}:")
        resto = valor
        idx = 0

        while resto > 0 and idx < len(cedulas):
            cedula_atual = cedulas[idx]
            qtd_cedulas = resto // cedula_atual
            
            if qtd_cedulas > 0:
                print(f"- {qtd_cedulas} cédula(s) de R$ {cedula_atual}")
                resto %= cedula_atual
                
            idx += 1

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")


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
    print("Digite as notas da turma (ou digite 'fim' para encerrar):")
    while True:
        entrada = input("Digite a nota: ").strip().lower()
        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
            else:
                print("Aviso: Nota fora do intervalo (0.0 a 10.0) ignorada.")
                continue
        except ValueError:
            print("Aviso: Entrada inválida. Digite um número ou 'fim'.")
            continue

    if len(notas) > 0:
        total_notas = len(notas)
        media = sum(notas) / total_notas
        maior = max(notas)
        menor = min(notas)

        print("\n--- RESUMO DOS DADOS DA TURMA ---")
        print(f"Total de notas válidas digitadas: {total_notas}")
        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota: {maior:.1f}")
        print(f"Menor nota: {menor:.1f}")
    else:
        print("\nNenhuma nota válida foi registrada.")


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
        except ValueError:
            print("Erro: Opção inválida! Digite um número do menu.")
            continue

        if opcao == 0:
            print("Encerrando o Sistema ITEAM. Até logo!")
            break

        elif opcao == 1:
            print("\n[1] Conversor de temperatura")
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"Resultado: {celsius}°C equivale a {fahrenheit:.1f}°F")
            except ValueError:
                print("Erro: Entrada de dados inválida.")

        elif opcao == 2:
            print("\n[2] Verificador de número primo")
            try:
                num = int(input("Digite um número inteiro: "))
                if num <= 1:
                    print(f"O número {num} não é primo.")
                else:
                    primo = True
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            primo = False
                            break
                    if primo:
                        print(f"O número {num} é primo! ✅")
                    else:
                        print(f"O número {num} não é primo. ❌")
            except ValueError:
                print("Erro: Entrada de dados inválida.")

        elif opcao == 3:
            print("\n[3] Analisador de senha simplificado")
            senha = input("Digite a senha para avaliar: ")
            tem_digito = any(char.isdigit() for char in senha)
            comprimento_ok = len(senha) >= 6

            print(f"- Pelo menos 6 caracteres: {'✅' if comprimento_ok else '❌'}")
            print(f"- Possui ao menos 1 número: {'✅' if tem_digito else '❌'}")

        elif opcao == 4:
            print("\n[4] Calculadora segura")
            try:
                n1 = float(input("Primeiro número: "))
                n2 = float(input("Segundo número: "))
                op = input("Operação (+, -, *, /): ").strip()
                if op == "+":
                    print(f"Resultado: {n1 + n2}")
                elif op == "-":
                    print(f"Resultado: {n1 - n2}")
                elif op == "*":
                    print(f"Resultado: {n1 * n2}")
                elif op == "/":
                    print(f"Resultado: {n1 / n2}")
                else:
                    print("Operação inválida.")
            except ZeroDivisionError:
                print("Erro: Divisão por zero!")
            except ValueError:
                print("Erro: Dados numéricos inválidos.")
        else:
            print("Opção inválida! Escolha um número de 0 a 4.")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Jennison Enthony Oliveira Diniz")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
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
    ex15_menu_sistema()