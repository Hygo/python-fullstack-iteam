"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Álefe Alves da Costa
Data    : 24/05/2026
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
    temp = float(input("Informe a temperatura em graus Celcius: "))

    print(f"Temperatura: {temp}°C")
    print("Classificação: ", end="")
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
    user = input("Informe o usuário: ")
    senha = input("Informe a senha: ")

    if user == "admin":
        if senha == "iteam2025":
            print("✅ Acesso liberado. Bem-vindo!")
        else: 
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
    num = int(input("Informe um número entre 1 a 10: "))

    print(f"=== Tabuada do {num} ===")
    for i in range(10):
        print(f"{num} x {i+1:>2} = {num*(i+1):>3}")


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
    cont = int(input("Informe um número inteiro positivo para a contagem regressiva: "))

    while cont >= 0:
        print(f"{cont}...", end=" ")
        cont-= 1
    print("\n🚀 Lançamento!")


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
    for i, prod in enumerate(estoque):
        if (prod == "Monitor"):
            print(f"Monitor encontrado na posição {i} da lista.")
            break
    
    if (i == len(estoque)):
        print("Produto não encontrado no estoque.")



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
    soma = 0.0
    media = 0.0
    invalidos = 0
    for number in leituras:
        if not (isinstance(number, float)):
            invalidos += 1
            continue
        soma += number
    
    media = soma / (len(leituras) - invalidos)

    print(f"A soma total dos valores válidos é {soma}")
    print(f"A média desses valores válidos é {media}")
    print(f"A quantidade de valores inválidos é {invalidos}")
    


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
        nota = int(input("Informe a nota do aluno (nota entre 0.0 a 10.0): "))

        if (10.0 >= nota >= 0.0):
            break

        print("Nota inválida.")
    
    if nota < 5.0:
        print("D – Insuficiente")
    elif nota <= 6.9:
        print("C – Regular")
    elif nota <= 8.9:
        print("B - Bom")
    else:
        print("A - Excelente")


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
        print("Bem-Vindo a Calculadora Segura")
        n1 = int(input("Informe o primeiro número: "))
        op = input("Informe a operação que deseja realizar (+, -, *, /): ")
        n2 = int(input("Informe o segundo número: "))
        

        if op not in ('+', '-', '*', '/'):
            raise ValueError("Operação inválida")

        if op == '+':
            resultado = n1 + n2
        elif op == '-':
            resultado = n1 - n2
        elif op == '*':
            resultado = n1 * n2
        elif op == '/':
            if n2 == 0:
                raise ZeroDivisionError
            resultado = n1 / n2


    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
    except ValueError as e:
        if str(e) == "Operação inválida":
            print("Erro: Operação inválida. Use apenas +, -, * ou /.")
        else:
            print("Erro: Valor digitado é inválido. Digite apenas números.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Calculadora encerrada.")


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
        for j in range (1, i + 1):
            print(j, end=" ")
        print()
    
    print()

    for i in range(5, 0, -1):
        for j in range (1, i + 1):
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
    c = 0
    acertou = False
    while c != 7:
        advinha = int(input(f"Tente adivinhar o número sorteado (1 a 100), você tem {7 - c} chances: "))
        if (advinha == numero_secreto):
            print(f"🎉 Parabéns! Você acertou em {c + 1} tentativas.")
            acertou = True
            break
        elif(c < 6):
            print("Você errou, ", end=" ")
            if(advinha > numero_secreto):
                print("o número secreto é menor.")
            else:
                print("o número secreto é maior.")
        c += 1

    if (not acertou):
        print(f"💀 Game over! O número era {numero_secreto}.")
        



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
        numero = int(input("Digite um número: "))
        if numero < 1:
            raise ValueError
            
        if numero == 1:
            print("1 não é núemro primo, nem composto.")
        else:
            primo = True
            divisor = 1
            limite = int(numero ** 0.5)
            for i in range(2, limite + 1):
                if numero % i == 0:
                    primo = False
                    divisor = i
                    break
            
            if primo:
                print(f"{numero} é um número primo.")
            else:
                print(f"{numero} não é primo, pois é divisível por {divisor}.")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro positivo.")


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
    senha = input("Digite a senha a ser analisada: ")

    comprimento = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False
    caracteres_especiais = "!@#$%^&*"

    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_digito = True
        elif char in caracteres_especiais:
            tem_especial = True

    print(f"Analisando: {senha}")
    print(f"{'✅' if comprimento else '❌'} Comprimento adequado ({len(senha)} caracteres)")
    print(f"{'✅' if tem_maiuscula else '❌'} Contém maiúscula")
    print(f"{'✅' if tem_minuscula else '❌'} Contém minúscula")
    print(f"{'✅' if tem_digito else '❌'} Contém número")
    print(f"{'✅' if tem_especial else '❌'} Contém caractere especial")

    if comprimento and tem_maiuscula and tem_minuscula and tem_digito and tem_especial:
        print("🔒 Senha FORTE!")
    else:
        print("🔓 Senha FRACA!")


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
        saque = int(input("Informe o valor do saque (múltiplo de 10, máximo R$3.000): "))
        if saque <= 0 or saque > 3000:
            print("Valor inválido. O limite do saque deve ser de até R$3.000.")
        elif saque % 10 != 0:
            print("Valor inválido. O valor deve ser múltiplo de 10.")
        else:
            print(f"💵 Saque: R$ {saque}")
            print("Cédulas utilizadas:")
            
            cedulas = [200, 100, 50, 20, 10]
            total_cedulas = 0
            valor_restante = saque
            
            for valor_cedula in cedulas:
                qtd_cedulas = valor_restante // valor_cedula
                if qtd_cedulas > 0:
                    print(f"  R${valor_cedula} → {qtd_cedulas} cédula(s)")
                    total_cedulas += qtd_cedulas
                    valor_restante %= valor_cedula
                        
            print(f"Total de cédulas: {total_cedulas}")
    except ValueError:
        print("Erro: Entrada inválida. Digite um valor numérico inteiro.")



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
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                notas.append(nota)
            else:
                print("Aviso: Nota fora do intervalo (0 a 10). Ignorada.")
                continue
        except ValueError:
            print("Aviso: Entrada não numérica. Ignorada.")
            pass

    if notas:
        total_notas = len(notas)
        media = sum(notas) / total_notas
        maior = max(notas)
        menor = min(notas)
        print(f"Total de notas válidas: {total_notas}")
        print(f"Média: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")
    else:
        print("Nenhuma nota válida foi registrada.")



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
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '0':
            print("Encerrando o sistema.")
            break
        elif opcao == '1':
            try:
                celsius = float(input("Temperatura em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"Resultado: {fahrenheit:.2f}°F")
            except ValueError:
                print("Erro: Entrada inválida.")
        elif opcao == '2':
            try:
                n = int(input("Digite um número: "))
                if n <= 1:
                    print("Não é primo.")
                else:
                    primo = True
                    for i in range(2, int(n**0.5) + 1):
                        if n % i == 0:
                            primo = False
                            break
                    print("É número primo." if primo else "Não é número primo.")
            except ValueError:
                print("Erro: Entrada inválida.")
        elif opcao == '3':
            senha = input("Senha: ")
            comprimento_ok = len(senha) >= 8
            tem_digito = any(c.isdigit() for c in senha)
            print(f"{'✅' if comprimento_ok else '❌'} Mínimo 8 caracteres")
            print(f"{'✅' if tem_digito else '❌'} Pelo menos 1 dígito")
            print("Senha adequada." if comprimento_ok and tem_digito else "Senha fraca.")
        elif opcao == '4':
            try:
                n1 = float(input("Número 1: "))
                n2 = float(input("Número 2: "))
                op = input("Operação (+, -, *, /): ")
                if op == '+':
                    print(f"Resultado: {n1 + n2}")
                elif op == '-':
                    print(f"Resultado: {n1 - n2}")
                elif op == '*':
                    print(f"Resultado: {n1 * n2}")
                elif op == '/':
                    print(f"Resultado: {n1 / n2}")
                else:
                    print("Operação inválida.")
            except ValueError:
                print("Erro: Entrada inválida.")
            except ZeroDivisionError:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida. Tente novamente.")
            continue


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Álefe Alves")
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
