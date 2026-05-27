"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): Felipe Spínola
Data    : 22/05/2026
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
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
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
    num = int(input("Digite um número inteiro: "))
    print(f"=== Tabuada do {num} ===")
    for i in range(1, 11):
        resultado = num * i
        print(f"{num} x {i:>2} = {resultado:>2}")


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    num = int(input("Digite um número inteiro positivo: "))
    while num >= 0:
        print(f"{num}...", end=" ")
        num -= 1
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

    encontrado = False
    for i, produto in enumerate(estoque):
        if produto == "Monitor":
            print(f"Monitor encontrado na posição {i}.")
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

    soma = 0.0
    validos = 0
    ignorados = 0
    
    for valor in leituras:
        if valor is None:
            ignorados += 1
            continue
        soma += valor
        validos += 1
        
    if validos > 0:
        media = soma / validos
    else:
        media = 0.0
        
    print(f"Soma dos valores válidos: {soma}")
    print(f"Média dos valores válidos: {media:.2f}")
    print(f"Total de registros ignorados: {ignorados}")


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
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
        if 0.0 <= nota <= 10.0:
            break
        print("Nota fora do intervalo permitido. Tente novamente.")

    if nota >= 9.0:
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
    """
    Solicita dois números e uma operação (+, -, *, /).
    Trata: ValueError, ZeroDivisionError, operação inválida.
    Usa else para exibir o resultado e finally para encerrar.
    """
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        
        if operacao not in ("+", "-", "*", "/"):
            raise ValueError("Operação inválida!")
            
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        else:
            resultado = num1 / num2
            
    except ValueError as err:
        if str(err) == "Operação inválida!":
            print("Erro: Operação inválida! Use apenas +, -, * ou /.")
        else:
            print("Erro: Entrada inválida. Digite números válidos.")
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
    """
    Gera o triângulo crescente:
        1
        1 2
        1 2 3
        ...
        1 2 3 4 5

    Desafio extra: gera também o triângulo decrescente logo abaixo.
    """
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

    tentativas = 1
    limite = 7
    acertou = False
    
    print("Pensei em um número entre 1 e 100. Você tem 7 tentativas para adivinhar!")
    
    while tentativas <= limite:
        try:
            palpite = int(input(f"Tentativa {tentativas}/{limite} - Digite seu palpite: "))
        except ValueError:
            print("Digite um número inteiro válido!")
            continue
            
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativas} tentativas.")
            acertou = True
            break
        elif palpite < numero_secreto:
            print("O número secreto é maior.")
        else:
            print("O número secreto é menor.")
            
        tentativas += 1
        
    if not acertou:
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
    try:
        num_str = input("Digite um número: ")
        n = int(num_str)
        if n <= 0:
            print("Erro: O número deve ser maior que zero.")
            return
            
        if n == 1:
            print("1 não é primo. Divisível apenas por ele mesmo. ❌")
            return
            
        primo = True
        divisor_encontrado = None
        
        limite = int(n ** 0.5)
        for i in range(2, limite + 1):
            if n % i == 0:
                primo = False
                divisor_encontrado = i
                break
                
        if primo:
            print(f"{n} é um número primo. ✅")
        else:
            print(f"{n} não é primo. Divisível por {divisor_encontrado}. ❌")
            
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro positivo.")


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
    print(f"\nAnalisando: {senha}")
    
    comprimento_ok = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False
    
    caracteres_especiais = "!@#$%^&*"
    
    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        elif caractere.islower():
            tem_minuscula = True
        elif caractere.isdigit():
            tem_digito = True
        elif caractere in caracteres_especiais:
            tem_especial = True
            
    if comprimento_ok:
        print(f"✅ Comprimento adequado ({len(senha)} caracteres)")
    else:
        print(f"❌ Mínimo de 8 caracteres (sua senha possui {len(senha)})")
        
    if tem_maiuscula:
        print("✅ Contém maiúscula")
    else:
        print("❌ Contém maiúscula")
        
    if tem_minuscula:
        print("✅ Contém minúscula")
    else:
        print("❌ Contém minúscula")
        
    if tem_digito:
        print("✅ Contém número")
    else:
        print("❌ Contém número")
        
    if tem_especial:
        print("✅ Contém caractere especial")
    else:
        print("❌ Contém caractere especial")
        
    if comprimento_ok and tem_maiuscula and tem_minuscula and tem_digito and tem_especial:
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

    try:
        valor = int(input("Digite o valor do saque: R$ "))
        if valor < 10 or valor > 3000:
            print("Erro: O limite de saque é de R$10 a R$3.000.")
            return
        if valor % 10 != 0:
            print("Erro: O valor deve ser múltiplo de R$10.")
            return
            
        print(f"💵 Saque: R$ {valor}")
        print("Cédulas utilizadas:")
        
        total_cedulas = 0
        valor_restante = valor
        i = 0
        
        while valor_restante > 0 and i < len(cedulas):
            cedula_atual = cedulas[i]
            if valor_restante >= cedula_atual:
                quantidade = valor_restante // cedula_atual
                valor_restante %= cedula_atual
                total_cedulas += quantidade
                print(f"  R${cedula_atual} → {quantidade} cédula(s)")
            i += 1
            
        print(f"Total de cédulas: {total_cedulas}")
        
    except ValueError:
        print("Erro: Digite apenas números inteiros válidos.")


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
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").strip().lower()
        if entrada == "fim":
            break
            
        try:
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print("Aviso: A nota deve estar entre 0.0 e 10.0. Ignorada.")
                continue
        except ValueError:
            print("Aviso: Entrada inválida. Digite uma nota numérica ou 'fim'. Ignorada.")
            continue
            
        notas.append(nota)
        
    if len(notas) > 0:
        total = len(notas)
        soma = 0.0
        maior = notas[0]
        menor = notas[0]
        
        for n in notas:
            soma += n
            if n > maior:
                maior = n
            if n < menor:
                menor = n
                
        media = soma / total
        
        print(f"\nResumo da turma:")
        print(f"Total de notas válidas: {total}")
        print(f"Média: {media:.2f}")
        print(f"Maior nota: {maior}")
        print(f"Menor nota: {menor}")
    else:
        print("Nenhuma nota válida foi inserida.")


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
            if opcao not in ["1", "2", "3", "4", "0"]:
                print("Opção inválida! Tente novamente.")
                continue
                
            if opcao == "0":
                print("Saindo do sistema. Até logo!")
                break
                
            elif opcao == "1":
                try:
                    celsius = float(input("Digite a temperatura em Celsius: "))
                    fahrenheit = (celsius * 1.8) + 32
                    print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")
                except ValueError:
                    print("Erro: digite um valor numérico para a temperatura.")
                    
            elif opcao == "2":
                try:
                    num = int(input("Digite um número inteiro: "))
                    if num < 2:
                        print(f"{num} não é primo.")
                    else:
                        primo = True
                        for i in range(2, num):
                            if num % i == 0:
                                primo = False
                                break
                        if primo:
                            print(f"{num} é um número primo!")
                        else:
                            print(f"{num} não é um número primo.")
                except ValueError:
                    print("Erro: digite um número inteiro válido.")
                    
            elif opcao == "3":
                senha = input("Digite a senha: ")
                comprimento_ok = len(senha) >= 8
                contem_digito = False
                for c in senha:
                    if c.isdigit():
                        contem_digito = True
                        break
                print(f"Comprimento (>= 8): {'✅' if comprimento_ok else '❌'}")
                print(f"Possui dígito: {'✅' if contem_digito else '❌'}")
                
            elif opcao == "4":
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))
                    op = input("Digite a operação (+, -, *, /): ")
                    if op == "+":
                        print(f"Resultado: {num1 + num2}")
                    elif op == "-":
                        print(f"Resultado: {num1 - num2}")
                    elif op == "*":
                        print(f"Resultado: {num1 * num2}")
                    elif op == "/":
                        if num2 == 0:
                            print("Erro: divisão por zero.")
                        else:
                            print(f"Resultado: {num1 / num2}")
                    else:
                        print("Erro: operação inválida.")
                except ValueError:
                    print("Erro: entrada inválida. Digite valores numéricos.")
                    
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): Felipe Spínola")
    print("=" * 50)

    # Descomente a linha do exercício que deseja testar:
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
