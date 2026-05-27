
"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Luciano dos Santos Nascimento
Data    : 26/05/2026
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
    temperatura = float(input("Digite a temperatura para podemos classificala: "))
    if temperatura < 0:
        print(f"Temperatura: {temperatura}\nClassificação: Congelante❄️")
    elif temperatura >= 0 and temperatura <= 14:
        print(f"Temperatura: {temperatura}\nClassificação: Frio⛄")
    elif temperatura > 14 and temperatura <= 24:
        print(f"Temperatura: {temperatura}\nClassificação: Agradavel😊")
    elif temperatura > 24 and temperatura <= 34:
        print(f"Temperatura: {temperatura}\nClassificação:  Quente🥵")
    else:
        print(f"Temperatura: {temperatura}\nClassificação: Muito quente🔥")



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
    usuario = "admin"
    senha = "iteam2025"
    user = input("Digite o usuario: ")
    password = input("Digite a senha: ")
    if usuario == user and senha == password:
        print("✅ Acesso liberado. Bem-vindo!")
    elif usuario == user and senha != password:
        print("❌ Senha incorreta.")
    else:
        print("❌ Usuário não encontrado.")



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
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]
    contador = 0
    notas = 0
    for l in leituras:
        if l == None:
            contador += 1
            continue
        notas += l
    print("Total: ", notas, " Media: ", notas/10, " Registros nones: ", contador)



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
    nota = float(input("Digite a nota: "))
    while nota >= 0 and nota <= 10 :
        if 9.0 <= nota >= 10.:
            print("A – Excelente")
        elif 7.0 <= nota >= 10.0:
            print("B – Bom")
        elif 5.0 <= nota >= 6.9:
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
    def somar(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a/b
   
    operadores = {
        "somar": somar,
        "subtrair": sub,
        "dividir": div,
        "multiplicar": mult
    }
    try:
        numero_um = int(input("Digite o primeiro numero: "))
        numero_dois = int(input("Digite o primeiro numero: "))
        operacao = input("Escolha uma operação\n1-Somar\n2-Dividir\n3-Multiplicar\n4-Subtrair\nFaça sua escolha: ")
        fn = operadores[operacao.lower()]
        resultado = fn(numero_um, numero_dois)
    except ZeroDivisionError:
        print("Não dá para dividir por zero")
    except ValueError:
        print("Valor invalido")
    except KeyError:
        print("Deu ruim, essa não é uma das opções")
    except IndexError as errou:
        print(f"Deu ruim {errou}")
    else:
        print(f"O resultado é {resultado}")
    finally:
        print("Está tudo acabado")

    



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
    numero = int(input("Digite um numero maior que zero: "))
    contador = 1
    while numero > 0:
        for i in range(1, contador+1):
            print(i, end=" ")
        print("")
        contador += 1
        numero -= 1


    


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
        tenta = int(input("Digite um numero"))
        if tenta == numero_secreto:
            print("Você acertou")
            break
        else:
            print("Errou tente novamente")


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
    try:
        numero = int(input("Digite um numero inteiro: "))
        if numero <= 1:
            print(f"{numero} não é primo.")
            return

        # O número 2 é o único primo par
        if numero == 2:
            print(f"{numero} é primo.")
            return

        # Elimina todos os outros números pares
        if numero % 2 == 0:
            print(f"{numero} não é primo.")
            return

        # Testa os divisores ímpares desde 3 até a raiz quadrada do número
        limite = int(math.sqrt(numero)) + 1
        for i in range(3, limite, 2):
            if numero % i == 0:
                print(f"{numero} não é primo.")
                return

        print(f"{numero} é primo.")

    except ValueError:
        print("❌ Entrada inválida. Digite um número inteiro.")


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
    senha = input("Digite sua senha: ")

    tem_minimo      = len(senha) >= 8
    tem_maiuscula   = any(c.isupper() for c in senha)
    tem_minuscula   = any(c.islower() for c in senha)
    tem_digito      = any(c.isdigit() for c in senha)
    tem_especial    = any(c in "!@#$%^&*" for c in senha)

    print("\n--- Relatório de Segurança ---")
    print(f"{'✅' if tem_minimo    else '❌'} Mínimo 8 caracteres")
    print(f"{'✅' if tem_maiuscula else '❌'} Pelo menos 1 letra maiúscula")
    print(f"{'✅' if tem_minuscula else '❌'} Pelo menos 1 letra minúscula")
    print(f"{'✅' if tem_digito    else '❌'} Pelo menos 1 dígito")
    print(f"{'✅' if tem_especial  else '❌'} Pelo menos 1 caractere especial (!@#$%^&*)")

    if all([tem_minimo, tem_maiuscula, tem_minuscula, tem_digito, tem_especial]):
        print("\n🔒 Senha FORTE!")
    else:
        print("\n⚠️  Senha FRACA. Corrija os critérios marcados com ❌.")


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
        valor = int(input("Digite o valor do saque (múltiplo de R$10, máx R$3.000): "))

        if valor <= 0:
            print("❌ O valor deve ser positivo.")
            return
        if valor > 3000:
            print("❌ Valor máximo permitido é R$3.000.")
            return
        if valor % 10 != 0:
            print("❌ O valor deve ser múltiplo de R$10.")
            return

        print(f"\n💵 Saque de R${valor} — cédulas utilizadas:")
        restante = valor
        for cedula in cedulas:
            quantidade = restante // cedula
            if quantidade > 0:
                print(f"   R${cedula:>3} × {quantidade}")
                restante -= cedula * quantidade

    except ValueError:
        print("❌ Entrada inválida. Digite um número inteiro.")


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
    print("Digite as notas dos alunos (ou 'fim' para encerrar):")
    while True:
        entrada = input("Nota: ").strip()

        if entrada.lower() == "fim":
            break

        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("⚠️  Nota inválida. Digite um valor entre 0 e 10.")
                continue
            notas.append(nota)
        except ValueError:
            print("⚠️  Entrada inválida. Digite um número ou 'fim' para encerrar.")
            continue

    if not notas:
        print("Nenhuma nota válida foi registrada.")
        return

    total  = sum(notas)
    media  = total / len(notas)
    maior  = max(notas)
    menor  = min(notas)

    print(f"\n--- Resultado da Turma ---")
    print(f"Total de notas : {len(notas)}")
    print(f"Soma           : {total:.1f}")
    print(f"Média          : {media:.2f}")
    print(f"Maior nota     : {maior:.1f}")
    print(f"Menor nota     : {menor:.1f}")


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
            opcao = input("Escolha uma opção: ").strip()
        except ValueError:
            print("❌ Entrada inválida.")
            continue

        if opcao == "0":
            print("👋 Saindo do sistema. Até logo!")
            break

        elif opcao == "1":
            # Conversor Celsius → Fahrenheit
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = celsius * 9 / 5 + 32
                print(f"🌡️  {celsius}°C = {fahrenheit:.1f}°F")
            except ValueError:
                print("❌ Valor inválido.")

        elif opcao == "2":
            # Verificador de número primo (versão simplificada)
            import math
            try:
                numero = int(input("Digite um número inteiro positivo: "))
                if numero < 2:
                    print(f"{numero} não é primo.")
                else:
                    primo = True
                    for i in range(2, int(math.sqrt(numero)) + 1):
                        if numero % i == 0:
                            primo = False
                            break
                    print(f"{'✅' if primo else '❌'} {numero} {'é' if primo else 'não é'} primo.")
            except ValueError:
                print("❌ Digite um número inteiro.")

        elif opcao == "3":
            # Analisador de senha (comprimento e dígito)
            senha = input("Digite a senha: ")
            tem_minimo = len(senha) >= 8
            tem_digito = any(c.isdigit() for c in senha)
            print(f"{'✅' if tem_minimo else '❌'} Mínimo 8 caracteres")
            print(f"{'✅' if tem_digito else '❌'} Pelo menos 1 dígito")
            if tem_minimo and tem_digito:
                print("🔒 Senha OK!")
            else:
                print("⚠️  Senha fraca.")

        elif opcao == "4":
            # Calculadora segura
            try:
                a = float(input("Primeiro número: "))
                b = float(input("Segundo número : "))
                op = input("Operação (+, -, *, /): ").strip()
                if op == "+":
                    resultado = a + b
                elif op == "-":
                    resultado = a - b
                elif op == "*":
                    resultado = a * b
                elif op == "/":
                    if b == 0:
                        raise ZeroDivisionError
                    resultado = a / b
                else:
                    print("❌ Operação inválida.")
                    continue
                print(f"✅ Resultado: {resultado}")
            except ValueError:
                print("❌ Valor inválido.")
            except ZeroDivisionError:
                print("❌ Não é possível dividir por zero.")

        else:
            print("❌ Opção inválida. Tente novamente.")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Luciano dos Santos Nascimento")
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
