import math;

"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Denym Andrade Queiroz
Data    : 20/05/2026
=============================================================

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
        < 0       → ❄️ Congelante
        0  a 14   → 🥶 Frio
        15 a 24   → 😊 Agradável
        25 a 34   → ☀️ Quente
        >= 35     → 🔥 Muito quente
    """
    celsius = float(input("Digite a temperatura em Celsius para Classificar: "))
    if celsius < 0:
        print("❄️ Congelante")
    elif celsius <= 14:
        print("🥶 Frio")
    elif celsius <= 24:
        print("😊 Agradável")
    elif celsius <= 34:
        print("☀️ Quente")
    else:
        print("🔥 Muito quente")
    pass


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
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    if usuario == "admin" and senha == "iteam2025":
        print("Acesso permitido!")
    else:
        print("Acesso negado!")

    pass


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    numero = int(input("Digite um número inteiro: "))
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

    pass


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    numero = int(input("Digite um número inteiro positivo: "))
    while numero >= 0:
        print(numero, end=" \n")
        numero -= 1
    print("🚀 Lançamento!" )
    pass


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

    for i, item in enumerate(estoque):
        print(f'{item} na posição {i}')
    pass


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
    total_valido = 0
    total_ignorado = 0
    media = 0.0

    for leitura in leituras:
        
        if leitura is None:
            total_ignorado += 1
            continue
        soma += leitura
        total_valido += 1
        media = soma / total_valido
        continue
    print(f"a soma é: {soma}")
    print(f"a média é: {media:.2f}")
    print(f"total válido: {total_valido}")
    print(f"total ignorado: {total_ignorado}")
    

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
    conceito = float(input("Digite a sua nota: "))
    while True:
        if conceito >= 9:
            print("Excelente")
            break
        elif conceito >= 7:
            print("Bom")
            break
        elif conceito >= 5:
            print("Regular")
            break
        else:
            print("Insuficiente")
        break
    pass


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
            
            raise ValueError("Operação inválida")


    except ValueError as erro:
        # Captura tanto letras digitadas no float() quanto a operação inválida do raise
        if "Operação inválida" in str(erro):
            print("[ERRO] A operação digitada não é válida! Use apenas +, -, * ou /.")
        else:
            print("[ERRO] Entrada inválida! Por favor, digite apenas números.")

    except ZeroDivisionError:
        # Captura a tentativa de divisão por zero
        print("[ERRO] Não é possível dividir um número por zero.")

    
    else:
        # Só executa se o bloco 'try' rodar perfeitamente sem nenhum erro
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")

    
    finally:
        # Roda SEMPRE, independente de ter dado erro ou sucesso
        print("Sessão finalizada. Obrigado por usar a calculadora!")

    pass


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
    altura = int(input("Digite a altura do triângulo: "))

    for i in range(1, altura + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    pass


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

   # numero = input("tente acertar o numero, vc tem 7 tentativas:")
    tentativas = 0
    while tentativas < 7:
        numero = int(input(f"tente acertar o numero, vc tem {7 - tentativas} tentativas:"))
        if numero == numero_secreto:
            print("acertou")
            break
        tentativas += 1
        
        
    print(numero_secreto)
    pass


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
    entrada = input("Digite um número inteiro positivo: ").strip()

    if entrada.isdigit():
        numero = int(entrada)

        if numero <= 1:
            print("O número deve ser maior que 1.")
        else:
        
            limite = int(numero ** 0.5)
            e_primo = True

        for i in range(2, limite + 1):
            if numero % i == 0:
                e_primo = False
                break

        if e_primo:
            print(f"{numero} é primo.")
        else:
            print(f"{numero} não é primo.")
    else:
        print("Erro: Digite apenas um número inteiro e positivo.")
    pass


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

# 1. Cria variáveis para checar se as regras foram atendidas (True ou False)
    tem_tamanho = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False

# Lista de caracteres especiais permitidos
    especiais = "!@#$%^&*"

# 2. Varre a senha caractere por caractere para validar os critérios
    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        elif letra.islower():
            tem_minuscula = True
        elif letra.isdigit():
            tem_digito = True
        elif letra in especiais:
            tem_especial = True

# 3. Exibe o relatório final usando operador ternário para escolher ✅ ou ❌
    print("\n--- RELATÓRIO DE SEGURANÇA ---")
    print(f"{'✅' if tem_tamanho else '❌'} Mínimo 8 caracteres")
    print(f"{'✅' if tem_maiuscula else '❌'} Pelo menos 1 maiúscula")
    print(f"{'✅' if tem_minuscula else '❌'} Pelo menos 1 minúscula")
    print(f"{'✅' if tem_digito else '❌'} Pelo menos 1 dígito")
    print(f"{'✅' if tem_especial else '❌'} Pelo menos 1 caractere especial (!@#$%^&*)")
    pass


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
    

    entrada = input("Digite o valor do saque (múltiplo de 10, máx R$3000): ").strip()

# 2. Valida se a entrada contém apenas números
    if entrada.isdigit():
        valor = int(entrada)
        
        if valor < 10 or valor > 3000:
            print("Erro: O valor deve ser entre R$ 10 e R$ 3000.")
        elif valor % 10 != 0:
            print("Erro: O valor deve ser múltiplo de R$ 10.")
        else:
            print(f"\nDispensando R$ {valor} em cédulas:")
        
        cedulas = [200, 100, 50, 20, 10]
        
        for cedula in cedulas:
        
            quantidade = valor // cedula  
            
            if quantidade > 0:
                print(f"- {quantidade} cédula(s) de R$ {cedula}")
                            
            valor = valor % cedula
    pass


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
        entrada = input("Digite a nota (ou 'fim' para encerrar): ").strip().lower()
    
   
        if entrada == 'fim':
            break
        
        
        try:
            nota = float(entrada)
            
            if nota < 0.0 or nota > 10.0:
                print("[AVISO] Nota inválida! Digite um valor entre 0.0 e 10.0.")
                continue  # Pula o restante do loop e pede a próxima nota
                
            notas.append(nota)
            
        except ValueError:
            print("[AVISO] Entrada inválida! Digite apenas números ou 'fim'.")
            continue

    if notas:
        total_notas = len(notas)
        media = sum(notas) / total_notas
        maior_nota = max(notas)
        menor_nota = min(notas)
        
        print("\n--- RESUMO DA TURMA ---")
        print(f"Total de notas válidas: {total_notas}")
        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota: {maior_nota:.1f}")
        print(f"Menor nota: {menor_nota:.1f}")
    else:
        print("\nNenhuma nota válida foi digitada.")
    pass


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
            opcao = input("Escolha uma opção: ").strip()
        
            # --- OPÇÃO 0: SAIR ---
            if opcao == "0":
                print("Saindo do sistema... Até logo!")
                break
                
            # --- OPÇÃO 1: CONVERSOR ---
            elif opcao == "1":
                try:
                    celsius = float(input("Digite a temperatura em °C: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"Resultado: {celsius:.2f}°C = {fahrenheit:.2f}°F")
                except ValueError:
                    print("[ERRO] Digite um número válido para a temperatura.")
                    
            # --- OPÇÃO 2: PRIMO ---
            elif opcao == "2":
                try:
                    numero = int(input("Digite um número inteiro positivo: "))
                    if numero <= 1:
                        print("O número deve ser maior que 1.")
                    else:
                        limite = int(numero ** 0.5)
                        e_primo = True
                        for i in range(2, limite + 1):
                            if numero % i == 0:
                                e_primo = False
                                break
                        if e_primo:
                            print(f"O número {numero} é PRIMO.")
                        else:
                            print(f"O número {numero} NÃO é primo.")
                except ValueError:
                    print("[ERRO] Digite apenas números inteiros.")
                    
            # --- OPÇÃO 3: SENHA ---
            elif opcao == "3":
                senha = input("Digite a senha para análise: ")
                tem_tamanho = len(senha) >= 8
                tem_digito = any(letra.isdigit() for letra in senha)
                
                print(f"{'✅' if tem_tamanho else '❌'} Mínimo 8 caracteres")
                print(f"{'✅' if tem_digito else '❌'} Pelo menos 1 dígito")
                
            # --- OPÇÃO 4: CALCULADORA ---
            elif opcao == "4":
                try:
                    n1 = float(input("Primeiro número: "))
                    n2 = float(input("Segundo número: "))
                    op = input("Operação (+, -, *, /): ").strip()
                    
                    if op == "+":
                        print(f"Resultado: {n1 + n2:.2f}")
                    elif op == "-":
                        print(f"Resultado: {n1 - n2:.2f}")
                    elif op == "*":
                        print(f"Resultado: {n1 * n2:.2f}")
                    elif op == "/":
                        if n2 == 0:
                            print("[ERRO] Não é possível dividir por zero.")
                        else:
                            print(f"Resultado: {n1 / n2:.2f}")
                    else:
                        print("[ERRO] Operação inválida.")
                except ValueError:
                    print("[ERRO] Digite valores numéricos válidos.")
                    
            else:
                print("[AVISO] Opção inválida! Escolha um número de 0 a 4.")
                
        except Exception as e:
            print(f"[ERRO inesperado]: {e}")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Denym Andrade Queiroz")
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
