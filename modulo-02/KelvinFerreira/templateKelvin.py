"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Kelvin Ferreira
Data    : 22/05/2026
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
    temperatura = float(input("Temperatura: "))

    if temperatura < 0:
        classificacao = "❄️ Congelante"
    elif temperatura <= 14:
        classificacao = "🥶 Frio"
    elif temperatura <= 24:
        classificacao = "😊 Agradável"
    elif temperatura <= 34:
        classificacao = "☀️ Quente"
    else:
        classificacao = "🔥 Muito quente"

    print(f"Temperatura: {temperatura:.1f}°C")
    print(f"Classificação: {classificacao}")


# ==============================================================
# EXERCÍCIO 02 – Validador de Acesso
# Conceitos: if aninhado, comparação de strings
# ==============================================================
def ex02_validador_acesso():
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "admin":
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
    numero = int(input("Digite um número: "))

    print(f"=== Tabuada do {numero} ===")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:>2} = {resultado:>3}")


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    numero = int(input("Digite um número positivo: "))

    while numero >= 0:
        print(f"{numero}...", end=" ")
        numero -= 1
    print("\n🚀 Lançamento!")


# ==============================================================
# EXERCÍCIO 05 – Buscador com break
# Conceitos: for, break, enumerate()
# ==============================================================
def ex05_buscador_break():
    estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

    encontrado = False
    for index, produto in enumerate(estoque):
        if produto == "Monitor":
            print(f"Produto encontrado na posição {index}.")
            encontrado = True
            break

    if not encontrado:
        print("Produto não encontrado no estoque.")


# ==============================================================
# EXERCÍCIO 06 – Filtro de Dados com continue
# Conceitos: for, continue, None, acumuladores
# ==============================================================
def ex06_filtro_continue():
    leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]

    soma = 0.0
    quantidade_validos = 0
    ignorados = 0

    for valor in leituras:
        if valor is None:
            ignorados += 1
            continue
        soma += valor
        quantidade_validos += 1

    media = soma / quantidade_validos if quantidade_validos > 0 else 0.0

    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Registros ignorados: {ignorados}")


# ==============================================================
# EXERCÍCIO 07 – Validação de Entrada com while
# Conceitos: while True, break, if/elif/else, float()
# ==============================================================
def ex07_validacao_nota():
    while True:
        nota_input = input("Digite a nota do aluno (0.0 a 10.0): ")
        try:
            nota = float(nota_input)
            if 0.0 <= nota <= 10.0:
                break
            print("Valor inválido. A nota deve ser entre 0.0 e 10.0.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    if 9.0 <= nota <= 10.0:
        conceito = "A – Excelente"
    elif nota >= 7.0:
        conceito = "B – Bom"
    elif nota >= 5.0:
        conceito = "C – Regular"
    else:
        conceito = "D – Insuficiente"

    print(f"Conceito: {conceito}")


# ==============================================================
# EXERCÍCIO 08 – Calculadora com try/except
# Conceitos: try/except/else/finally, ValueError, ZeroDivisionError
# ==============================================================
def ex08_calculadora_segura():
    try:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
        operacao = input("Operação (+, -, *, /): ")
        
        if operacao not in ('+', '-', '*', '/'):
            raise ValueError("Operação inválida.")
            
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

    except ValueError as e:
        if "Operação inválida" in str(e):
            print("Erro: Operação inválida.")
        else:
            print("Erro: Entrada inválida. Digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Calculadora encerrada.")


# ==============================================================
# EXERCÍCIO 09 – Padrão Numérico com for aninhado
# Conceitos: for aninhado, range(), print com end=
# ==============================================================
def ex09_padrao_numerico():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# ==============================================================
# EXERCÍCIO 10 – Jogo de Adivinhação
# Conceitos: while, contador, random, if/elif/else
# ==============================================================
def ex10_jogo_adivinhacao():
    import random

    numero_secreto = random.randint(1, 100)
    tentativas = 1
    max_tentativas = 7
    acertou = False

    while tentativas <= max_tentativas:
        try:
            palpite = int(input(f"Round {tentativas}/{max_tentativas} - Seu palpite (1 a 100): "))
            if palpite == numero_secreto:
                print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
                acertou = True
                break
            elif palpite < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")
            tentativas += 1
        except ValueError:
            print("Digite um número inteiro válido.")

    if not acertou:
        print(f"💀 Game over! O número era {numero_secreto}.")


# ==============================================================
# EXERCÍCIO 11 – Verificador de Número Primo
# Conceitos: for, break, try/except, otimização com √n
# ==============================================================
def ex11_numero_primo():
    try:
        numero = int(input("Digite um número: "))
        if numero < 1:
            raise ValueError
            
        if numero == 1:
            print("1 não é primo nem composto. ❌")
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
                print(f"{numero} é um número primo. ✅")
            else:
                print(f"{numero} não é primo. Divisível por {divisor}. ❌")

    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro positivo.")


# ==============================================================
# EXERCÍCIO 12 – Analisador de Senha Forte
# Conceitos: for, if, booleanos, métodos de string
# ==============================================================
def ex12_analisador_senha():
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
    try:
        saque = int(input("Valor do saque: "))
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
    notas_validas = []

    while True:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
        if entrada == 'fim':
            break
        try:
            nota = float(entrada)
            if 0.0 <= nota <= 10.0:
                notas_validas.append(nota)
            else:
                print("Aviso: Nota fora do intervalo (0 a 10). Ignorada.")
                continue
        except ValueError:
            print("Aviso: Entrada não numérica. Ignorada.")
            pass

    if notas_validas:
        total_notas = len(notas_validas)
        media = sum(notas_validas) / total_notas
        maior = max(notas_validas)
        menor = min(notas_validas)
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
    while True:
        print("\n=============================")
        print("   SISTEMA ITEAM - MENU    ")
        print("=============================")
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")
        print("=============================")
        
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
    print(f"Aluno(a): <SEU NOME>")
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