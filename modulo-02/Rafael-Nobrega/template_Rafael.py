"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <Rafael Nóbrega de Lima>
Data    : <DATA DE ENTREGA>
=============================================================

INSTRUÇÕES:
  1. Substitua <Rafael Nóbrega de Lima> e <DATA DE ENTREGA> acima.
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
    temp = float(input("Digite uma temperatura, por favor: "))

    if temp < 0:
        print(f"- {temp} está  Congelante ❄️")
    elif  0 > temp < 14:
        print(f"- {temp} está  Frio 🥶")
    elif 15 > temp < 24:
        print(f"- {temp} está  Agradável 😊")
    elif 25 > temp < 34:
        print(f"- {temp} está  Quente ☀️🥵")
    else:
        print(f"- {temp} está  Muito Quente 🔥🔥")

    
# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    """
    Solicita usuário e senha e valida o acesso.

    Credenciais corretas:
        usuário → "admin"
        senha   → "iteam2026"
    """
    # SUA SOLUÇÃO AQUI

    usuario = str(input("Digite o seu usuário: "))
    senha = str(input("Digite a sua senha: "))

    if usuario == "admin":
        if senha == "iteam2026":
            print("Acesso concedido!!")
        else:
            print("Senha Incorreta!!")
    else:
        print("Usuário incorreto!!")
    


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    tabuada = (int(input("Você quer a tabuada de qual número ? ")))
    print("=" * 50)

    for i in range(11):
        print(f"{tabuada} x {i} = { tabuada * i}")

    print("=" * 50)


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
    num_int = int(input("Digite um número inteiro positivo"))

    while num_int >= 0:
        print(num_int, end="...\n")
        num_int -= 1
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
    for i, estoque in  enumerate(estoque):
        if estoque == "Monitor":
            print(f"O produto {estoque} está no indice {i + 1}")
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

    for leitura in leituras:
        if leitura == None:
            continue
        else:
            print(leitura)



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
        nota = float(input("Digite a sua nota:"))

        if nota < 0 or nota > 10:
            print("Nota fora do limite (0 - 10). Tente outra nota")
            continue

        if nota >= 9:
            print(f"A sua nota {nota} tem o conceito A| Excelente")
            break
        elif nota >= 7:
            print(f"A sua nota {nota} tem o conceito B| Bom")
            break
        elif nota  >= 5:
            print(f"A sua nota {nota} tem o conceito C| Regular")
            break
        elif nota < 5:
            print(f"A sua nota {nota} tem o conceito D| Insuficiente")
            break



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
        num1 = int(input("Digite o primeiro número"))
        num2 = int(input("Digite o segundo número"))
        op = str(input("Qual operação que você quer fazer ? (+, -, *, /)"))

        if op not in ['+','-','*','/']:
            raise ValueError('Operação desconhecida!!')
        
        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            resultado = num1 - num2
        elif op == '*':
            resultado = num1 * num2
        elif op == '/':
            resultado = num1 / num2

    except ZeroDivisionError:
        print("Error: Não é possivel fazer a divisão por zero.")
    
    except ValueError as erro:
        if str(erro) == "Operação desconhecida!!":
            print("ERROR: A operação digitada não é valida. Use apenas +,-,* ou /.")
        else:
            print("ERROR: Você deve digitar número válidos.")

    else:
        print(f"Resultado da operação é {resultado}")
    
    finally:
        print("Calculadora encerrada.")
        print("=" * 50)



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
    for linha in range(1, 6):
        
        for coluna in range(1, linha + 1):
            print(coluna, end=" ")

        print()
    
    for linha in range(5, 0, -1):
        
        for coluna in range(1, linha + 1):
            print(coluna, end=" ")

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

    print("-------------------JOGO DA ADIVINHAÇÃO---------------------")
    print("Pensei em um número entre 1 e 100. Você tem 7 tentativas para adivinhar!")
    print("-" * 50)

    for tentativa in range(1,8):
        palpite = int(input(f"Tentativa: {tentativa}/7 - Digite seu palpite: "))

        if palpite == numero_secreto:
            print(f"\n Parabéns!! Você acertou em {tentativa} tentativas. O número era {numero_secreto}")
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR que seu palpite")
        else:
            print("O número secreto é MENOR do que seu palpite")   

        print("-" * 50)

    else:
        print(f"\n Fim de Jogo!! Suas Tentativas acabaram. O número era {numero_secreto}")



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
    while True:
        try:
            num = int(input("Digite um número inteiro positivo: "))

            if num <= 0:
                raise ValueError("O número digitado deve ser positivo.")
            break
        
        except ValueError:
            print("ERROR: Entrada Inválida!! Digite um número inteiro maior do que zero. \n")

    if num == 1:
        eh_primo = False
    else:
        eh_primo = True

        limite = int(num ** 0.5)

        for i in range(2, limite + 1):
            if num % i == 0:
                eh_primo = False
                break

    
    if eh_primo:
        print(f"O {num} é PRIMO. ✅")
    else:
        print(f"O {num} NÃO é PRIMO. ❌")
        



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

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    especiais = "!@#$%^&*"

    comprimento_ok = len(senha) >= 8

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in especiais:
            tem_especial = True

    print(f"\n Analisando: {senha}")

    if comprimento_ok:
        print(f"✅ comprimento adequado ({len(senha)}) caracteres)")
    else:
        print(f"❌ muito curta ( possui apenas {len(senha)}) caracteres, mínimo é 8)")

    print("✅ Contém maiúscula" if tem_maiuscula else "❌ Não contém maiúscula")
    print("✅ Contém minúscula" if tem_minuscula else "❌ Não contém minúscula")
    print("✅ Contém número" if tem_numero else "❌ Não contém número")
    print("✅ Contém caracteres especiais" if tem_especial else "❌ Não contém caractere especial")

    if comprimento_ok and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        print("🔒 senha FORTE!")
    else:
        print("⚠️  senha FRACA! Ajuste os itens marcados com ❌")



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
    while True:
        try:
            valor = int(input("Digite o valor que deseja sacar (R$): "))

            if valor <= 0:
                print("ERROR: o Valor do saque deve ser maior que zero. \n")
                continue
            elif valor > 3000:
                print("ERROR: O limite máximo por saque é de R$ 3.000. \n")
                continue
            elif valor % 10 != 0:
                print("ERROR: Este caixa possui apenas cédulas de R$ 200, R$ 100, R$ 50, R$ 20 e R$ 10.")
                print("Por favor, digite um valor múltiplo de 10.\n")
                continue

            break
        except ValueError:
            print("ERROR: Entrada Inválida! Digite apenas números inteirso. \n")

    valor_saque = valor

    cedulas = [200, 100, 50, 20, 10]
    total_cedulas_entregues = 0

    print(f"\n💵 Saque: R$ {valor_saque}")
    print("Cédulas utilizadas:")

    posicao = 0
    while valor > 0:
        cedula_atual = cedulas[posicao]

        quantidade_cedulas = valor // cedula_atual

        if quantidade_cedulas > 0:
            print(f" R$ {cedula_atual} -> {quantidade_cedulas} cédula(s)")
            total_cedulas_entregues += quantidade_cedulas

            valor %= cedula_atual
        
        posicao += 1

    print(f"Total de cédulas: {total_cedulas_entregues}")


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
    notasValidas = []

    print("-------------SISTEMA DE NOTAS DA TURMA-----------")
    print("Digite as notas uma por uma. Para encerrar o programa, digite 'fim'.\n")

    while True:
        entrada = input("Digite uam nota (0 a 10): ").strip().lower()

        if entrada == "fim":
            break

        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("⚠️ Aviso: Nota Inválida! A nota inserida no sistem só pode ser entre 0 e 10")
                continue 

            notasValidas.append(nota)

        except ValueError:
            print("ERROR: Entrada não númerica inválida (exceto 'fim'). Tente novamente com uma nota válida.\n")
            continue

    print("\n" + "=" * 35)
    print("          RELATÓRIO DA TURMA         ")
    print("=" * 35)

    totalNotas = len(notasValidas)

    if totalNotas > 0:
        media = sum(notasValidas) / totalNotas
        maiorNota = max(notasValidas)
        menorNota = min(notasValidas)

        print(f"Total de notas válidas: {totalNotas}")
        print(f"Média da turma: {media:.1f}")
        print(f"Maior nota da Turma: { maiorNota:.1f}")
        print(f"Menor nota da Turma: {menorNota:.1f}")
    else:
        print("Nenhuma nota válida foi registrada no sistema.")

    print("=" * 35)


        


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
            print("⚠️ Erro: Digite apenas números inteiros!")
            continue  

        if opcao == 0:
            print("\nEncerrando o Sistema ITEAM. Até logo!")
            break 

        elif opcao == 1:
            print("\n--- [1] Conversor de Temperatura (C° para F°) ---")
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"Resultado: {celsius}°C equivale a {fahrenheit:.1f}°F")
            except ValueError:
                print("⚠️ Entrada inválida! Retornando ao menu.")

        elif opcao == 2:
            print("\n--- [2] Verificador de Número Primo ---")
            try:
                num = int(input("Digite um número inteiro positivo: "))
                if num <= 1:
                    print("Não é primo.")
                else:
                    eh_primo = True
                    for i in range(2, int(num ** 0.5) + 1):
                        if num % i == 0:
                            eh_primo = False
                            break
                    print(f"O número {num} é PRIMO!" if eh_primo else f"O número {num} NÃO é primo.")
            except ValueError:
                print("⚠️ Entrada inválida! Retornando ao menu.")

        elif opcao == 3:
            print("\n--- [3] Analisador de Senha ---")
            senha = input("Digite a senha para testar: ")
            if len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.isdigit() for c in senha):
                print("🔒 Senha Forte! (Atende aos requisitos básicos)")
            else:
                print("⚠️ Senha Fraca! Precisa de pelo menos 8 dígitos, 1 maiúscula e 1 número.")

        elif opcao == 4:
            print("\n--- [4] Calculadora Segura ---")
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                op = str(input("Qual operação que você quer fazer ? (+, -, *, /): "))

                if op not in ['+','-','*','/']:
                    raise ValueError('Operação desconhecida!!')
                
                if op == '+':
                    resultado = n1 + n2
                elif op == '-':
                    resultado = n1 - n2
                elif op == '*':
                    resultado = n1 * n2
                elif op == '/':
                    resultado = n1 / n2

            except ZeroDivisionError:
                print("❌ Erro: Não é possível dividir por zero!")
            except ValueError:
                print("⚠️ Erro: Digite apenas valores numéricos!")
            finally:
                print(f"Resultado da operação é {resultado}")

        else:
            print("⚠️ Opção inválida! Escolha um número de 0 a 4.")
            continue



# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): <Rafael Nóbrega>")
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
    # ex15_menu_sistema()
