"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <Amanda de Brito Barbosa>
Data    : <23.05.2026>
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
    temperatura = float(input("Temperatura: "))

    if temperatura < 0:
        classificacao = "❄️ Congelante"
    elif 0 <= temperatura <= 14:
        classificacao = "🥶 Frio"
    elif 15 <= temperatura <= 24:
        classificacao = "😊 Agradável"
    elif 25 <= temperatura <= 34:
        classificacao = "☀️ Quente"
    else:
        classificacao = "🔥 Muito quente"

    print(f"Classificação: {classificacao}")


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
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
    numero = int(input("Digite um número para ver a tabuada: "))

    print(f"\n=== Tabuada do {numero} ===")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:>2} = {resultado:>3}")


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
    numero = int(input("Digite um número inteiro positivo: "))

    while numero >= 0:
        print(f"{numero}...", end=" ")
        numero -= 1

    print()
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
    encontrado = False

    for posicao, produto in enumerate(estoque):
        if produto == "Monitor":
            print(f"Monitor encontrado na posição {posicao}.")
            encontrado = True
            break

    if not encontrado:
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
    soma_validos = 0.0
    quantidade_validos = 0
    total_ignorados = 0

    for valor in leituras:
        if valor is None:
            total_ignorados += 1
            continue
            
        soma_validos += valor
        quantidade_validos += 1

    media_validos = soma_validos / quantidade_validos if quantidade_validos > 0 else 0.0

    print(f"Soma dos valores válidos: {soma_validos:.1f}")
    print(f"Média dos valores válidos: {media_validos:.2f}")
    print(f"Total de registros ignorados: {total_ignorados}")


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
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
        if 0.0 <= nota <= 10.0:
            break
        print("Nota inválida! Tente novamente.")

    if 9.0 <= nota <= 10.0:
        conceito = "A – Excelente"
    elif 7.0 <= nota <= 8.9:
        conceito = "B – Bom"
    elif 5.0 <= nota <= 6.9:
        conceito = "C – Regular"
    else:
        conceito = "D – Insuficiente"

    print(f"Conceito: {conceito}")


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
        num1 = float(input("Digite the primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ").strip()
        num2 = float(input("Digite o segundo número: "))

        if operacao not in ('+', '-', '*', '/'):
            raise ValueError("Operação inválida")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                raise ZeroDivisionError
            resultado = num1 / num2

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
    # Padrão Crescente
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    print()

    # Padrão Invertido
    for i in range(5, 0, -1):
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
    tentativas_maximas = 7
    rodada = 1
    acertou = False

    print("==================================================")
    print("       JOGO DE ADIVINHAÇÃO (1 A 100)              ")
    print("==================================================")
    print(f"Você tem {tentativas_maximas} tentativas para adivinhar o número secreto.\n")

    while rodada <= tentativas_maximas:
        palpite = int(input(f"Rodada {rodada}/{tentativas_maximas} - Digite seu palpite: "))
        
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {rodada} tentativas.")
            acertou = True
            break
        elif palpite < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
            
        rodada += 1
        print("-" * 50)

    if not acertou:
        print(f"\n💀 Game over! O número era {numero_secreto}.")
    print("==================================================")


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
        if numero <= 0:
            raise ValueError("O número deve ser positivo.")

        if numero == 1:
            is_primo = False
            divisor_encontrado = None
        else:
            is_primo = True
            divisor_encontrado = None
            limite = int(numero ** 0.5)
            
            for i in range(2, limite + 1):
                if numero % i == 0:
                    is_primo = False
                    divisor_encontrado = i
                    break

        if is_primo:
            print(f"{numero} é um número primo. ✅")
        else:
            if divisor_encontrado:
                print(f"{numero} não é primo. Divisível por {divisor_encontrado}. ❌")
            else:
                print(f"{numero} não é primo. ❌")

    except ValueError as e:
        if "invalid literal" in str(e):
            print("Erro: Entrada inválida! Digite apenas números inteiros.")
        else:
            print(f"Erro: {e}")


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
    caracteres_especiais = "!@#$%^&* "

    tem_minimo_caracteres = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_numero = True
        elif caractere in caracteres_especiais:
            tem_especial = True

    print(f"\nAnalisando: {senha}")

    if tem_minimo_caracteres:
        print(f"✅ Comprimento adequado ({len(senha)} caracteres)")
    else:
        print(f"❌ Muito curta ({len(senha)} caracteres) - Mínimo de 8")

    print(f"{'✅' if tem_maiuscula else '❌'} Contém maiúscula")
    print(f"{'✅' if tem_minuscula else '❌'} Contém minúscula")
    print(f"{'✅' if tem_numero else '❌'} Contém número")
    print(f"{'✅' if tem_especial else '❌'} Contém caractere especial")

    if tem_minimo_caracteres and tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        print("🔒 Senha FORTE!")
    else:
        print("⚠️ Senha FRACA!")


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
        valor_input = input("Saque: R$ ")
        valor = int(valor_input)

        if valor <= 0:
            print("Erro: O valor do saque deve ser maior que zero.")
        elif valor % 10 != 0:
            print("Erro: Valor indisponível. Este caixa trabalha apenas com cédulas de R$200, R$100, R$50, R$20 e R$10.")
        elif valor > 3000:
            print("Erro: O valor máximo permitido por saque é R$ 3.000.")
        else:
            print("Cédulas utilizadas:")
            idx = 0
            total_cedulas = 0
            montante = valor

            while montante > 0 and idx < len(cedulas):
                cedula_atual = cedulas[idx]
                if montante >= cedula_atual:
                    qtd_cedulas = montante // cedula_atual
                    montante %= cedula_atual
                    total_cedulas += qtd_cedulas
                    print(f"  R${cedula_atual} → {qtd_cedulas} cédula(s)")
                idx += 1

            print(f"Total de cédulas: {total_cedulas}")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números inteiros.")


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
        
        if entrada == "fim":
            break
            
        try:
            nota = float(entrada)
            
            if nota < 0 or nota > 10:
                print("Aviso: Nota fora do intervalo permitido (0 a 10). Ignorada.")
                continue
                
            notas.append(nota)
            
        except ValueError:
            print("Aviso: Entrada não numérica inválida. Ignorada.")
            continue

    print("\n=========================================")
    print("          RESUMO DA TURMA                ")
    print("=========================================")

    total_notas = len(notas)

    if total_notas > 0:
        media = sum(notas) / total_notas
        maior_nota = max(notas)
        menor_nota = min(notas)
        
        print(f"Total de notas válidas : {total_notas}")
        print(f"Média da turma         : {media:.2f}")
        print(f"Maior nota registrada  : {maior_nota:.1f}")
        print(f"Menor nota registrada  : {menor_nota:.1f}")
    else:
        print("Nenhuma nota válida foi registrada.")
    print("=========================================")


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
            opcao_input = input("Escolha uma opção: ").strip()
            opcao = int(opcao_input)
        except ValueError:
            print("Aviso: Entrada inválida. Por favor, digite apenas números.")
            continue

        if opcao == 0:
            print("Encerrando o sistema... Até logo!")
            break
            
        elif opcao == 1:
            print("\n--- [1] Conversor de Temperatura ---")
            try:
                celsius = float(input("Digite a temperatura em Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"Temperatura equivalente: {fahrenheit:.1f}°F")
            except ValueError:
                print("Aviso: Valor numérico inválido.")
                
        elif opcao == 2:
            print("\n--- [2] Verificador de Número Primo ---")
            try:
                num = int(input("Digite um número inteiro positivo: "))
                if num <= 1:
                    print("Não é primo.")
                else:
                    primo = True
                    for i in range(2, int(num**0.5) + 1):
                        if num % i == 0:
                            primo = False
                            break
                    print("É um número primo. ✅" if primo else "Não é primo. ❌")
            except ValueError:
                print("Aviso: Entrada inválida.")
                
        elif opcao == 3:
            print("\n--- [3] Analisador de Senha ---")
            senha = input("Digite uma senha para analisar: ")
            comprimento_ok = len(senha) >= 8
            possui_digito = any(c.isdigit() for c in senha)
            
            if comprimento_ok and possui_digito:
                print("Senha atende aos critérios básicos! ✅")
            else:
                if not comprimento_ok:
                    print("Erro: A senha precisa ter pelo menos 8 caracteres. ❌")
                if not possui_digito:
                    print("Erro: A senha precisa conter pelo menos 1 número. ❌")
                
        elif opcao == 4:
            print("\n--- [4] Calculadora Segura ---")
            try:
                n1 = float(input("Digite o primeiro número: "))
                op = input("Digite a operação (+, -, *, /): ").strip()
                n2 = float(input("Digite o segundo número: "))
                
                if op == '+':
                    print(f"Resultado: {n1 + n2}")
                elif op == '-':
                    print(f"Resultado: {n1 - n2}")
                elif op == '*':
                    print(f"Resultado: {n1 * n2}")
                elif op == '/':
                    if n2 == 0:
                        print("Erro: Divisão por zero detectada.")
                    else:
                        print(f"Resultado: {n1 / n2}")
                else:
                    print("Aviso: Operação matemática inválida.")
            except ValueError:
                print("Aviso: Digite apenas números válidos.")
                
        else:
            print("Aviso: Opção inválida. Escolha um número de 0 a 4.")
            continue


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Amanda de Brito Barbosa")
    print("=" * 50)
