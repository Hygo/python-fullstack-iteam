"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <SEU NOME COMPLETO AQUI>
Data    : <DATA DE ENTREGA>
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

    # Leitura da temperatura
    temperatura = float(input("Digite a temperatura em °C: "))
    
    # Classificação da temperatura usando estrutura if/elif/else
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
    
    # Exibição do resultado
    print(f"Temperatura: {temperatura}°C")
    print(f"Classificação: {classificacao}")

# Chamada da função para teste
if __name__ == "__main__":
    ex01_classificador_temperatura()

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
    # SUA SOLUÇÃO AQUI

    # Leitura das credenciais
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    
    # Validação com if aninhado
    if usuario == "admin":
        if senha == "iteam2025":
            print("✅ Acesso permitido!")
        else:
            print("❌ Senha incorreta!")
    else:
        print("❌ Usuário não encontrado!")
    
    # Versão alternativa com operador lógico (sem aninhamento)
    # if usuario == "admin" and senha == "iteam2025":
    #     print("✅ Acesso permitido!")
    # else:
    #     print("❌ Acesso negado!")

# Chamada da função para teste
if __name__ == "__main__":
    ex02_validador_acesso()
    pass


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    
    # SUA SOLUÇÃO AQUI

    numero = int(input("Número: "))
    inicio = int(input("Início da tabuada: "))
    fim = int(input("Fim da tabuada: "))
    
    print(f"\nTABUADA DO {numero} (do {inicio} ao {fim})")
    print("-" * 35)
    
    for i in range(inicio, fim + 1):
        print(f"{numero} × {i:2} = {numero * i:3}")
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

    # Leitura do número
    numero = int(input("Digite um número inteiro positivo para contagem regressiva: "))
    
    # Validação para garantir número positivo
    while numero < 0:
        print("❌ Erro: Digite um número positivo!")
        numero = int(input("Digite um número inteiro positivo: "))
    
    # Contagem regressiva
    contador = numero
    
    while contador >= 0:
        if contador > 0:
            # print com end=' ' para não pular linha e adicionar espaço
            print(contador, end=' ')
        else:
            # Quando chegar a 0, exibe mensagem de lançamento
            print("🚀 Lançamento!")
        contador -= 1  # Decrementa o contador

# Chamada da função para teste
if __name__ == "__main__":
    ex04_contador_regressivo()
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
    for i, item in enumerate(estoque):
        if item == "Monitor":
            print(f"✅ Item encontrado na posição {i}")
            break
    else:
        print("❌ Item não encontrado!")
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
    soma = 0
    contador = 0
    ignorados = 0

    for valor in leituras:
        if valor is None:
            ignorados += 1
            continue
        soma += valor
        contador += 1

    media = soma / contador if contador > 0 else 0
    
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Valores ignorados: {ignorados}")
    # SUA SOLUÇÃO AQUI
    pass


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
        nota = float(input("Digite a nota (0.0 a 10.0): "))
        
        if 0.0 <= nota <= 10.0:
            break
        print("❌ Nota inválida! Digite um valor entre 0.0 e 10.0.")
    
    if nota >= 9.0:
        print("Conceito: A – Excelente")
    elif nota >= 7.0:
        print("Conceito: B – Bom")
    elif nota >= 5.0:
        print("Conceito: C – Regular")
    else:
        print("Conceito: D – Insuficiente")
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
    # SUA SOLUÇÃO AQUI  
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            print("❌ Operação inválida!")
            return
        
    except ValueError:
        print("❌ Erro: Digite números válidos!")
    except ZeroDivisionError:
        print("❌ Erro: Divisão por zero não permitida!")
    else:
        print(f"✅ Resultado: {num1} {operacao} {num2} = {resultado:.2f}")
    finally:
        print("🔒 Calculadora encerrada.")
    
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
    # SUA SOLUÇÃO AQUI
     # Triângulo crescente
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    
    print()  # Linha em branco
    
    # Triângulo decrescente (desafio extra)
    for i in range(5, 0, -1):
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

    tentativas = 7
    
    for tentativa in range(1, tentativas + 1):
        palpite = int(input(f"Tentativa {tentativa}/{tentativas}: Adivinhe o número (1-100): "))
        
        if palpite == numero_secreto:
            print(f"🎉 Parabéns! Você acertou em {tentativa} tentativas!")
            break
        elif palpite < numero_secreto:
            print("📈 O número é MAIOR!")
        else:
            print("📉 O número é MENOR!")
    else:
        print(f"❌ Fim de jogo! O número era {numero_secreto}.")

    # SUA SOLUÇÃO AQUI
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
    # SUA SOLUÇÃO AQUI
    try:
        n = int(input("Digite um número inteiro positivo: "))
        
        if n <= 0:
            print("❌ Número inválido! Digite um número positivo maior que zero.")
            return
        
        if n == 1:
            print(f"❌ O número {n} NÃO é primo.")
            return
        
        primo = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                primo = False
                break
        
        if primo:
            print(f"✅ O número {n} é PRIMO!")
        else:
            print(f"❌ O número {n} NÃO é primo.")
            
    except ValueError:
        print("❌ Erro! Digite um número inteiro válido.")
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
    # SUA SOLUÇÃO AQUI

    senha = input("Digite a senha para análise: ")
    
    tem_minimo = len(senha) >= 8
    tem_maiuscula = False
    tem_minuscula = False
    tem_digito = False
    tem_especial = False
    
    especiais = "!@#$%^&*"
    
    for char in senha:
        if char.isupper():
            tem_maiuscula = True
        elif char.islower():
            tem_minuscula = True
        elif char.isdigit():
            tem_digito = True
        elif char in especiais:
            tem_especial = True
    
    print("\n" + "="*40)
    print("RELATÓRIO DA SENHA")
    print("="*40)
    print(f"✓ Mínimo 8 caracteres:         {'✅' if tem_minimo else '❌'}")
    print(f"✓ Pelo menos 1 maiúscula:      {'✅' if tem_maiuscula else '❌'}")
    print(f"✓ Pelo menos 1 minúscula:      {'✅' if tem_minuscula else '❌'}")
    print(f"✓ Pelo menos 1 dígito:         {'✅' if tem_digito else '❌'}")
    print(f"✓ Pelo menos 1 especial:       {'✅' if tem_especial else '❌'}")
    print("="*40)
    
    if all([tem_minimo, tem_maiuscula, tem_minuscula, tem_digito, tem_especial]):
        print("✅ SENHA FORTE! Todos os critérios atendidos.")
    else:
        print("❌ SENHA FRACA! Revise os critérios não atendidos.")
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
    cedulas = [200, 100, 50, 20, 10]

    # SUA SOLUÇÃO AQUI

    try:
        valor = int(input("Digite o valor do saque (R$10 a R$3.000, múltiplo de 10): "))
        
        if valor < 10 or valor > 3000:
            print("❌ Valor inválido! O saque deve ser entre R$10 e R$3.000.")
            return
        
        if valor % 10 != 0:
            print("❌ Valor inválido! O saque deve ser múltiplo de R$10.")
            return
        
        print(f"\n💵 Saque de R${valor:.2f}")
        print("-" * 30)
        
        for cedula in cedulas:
            quantidade = valor // cedula
            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R$ {cedula}")
                valor %= cedula
        
        print("-" * 30)
        
    except ValueError:
        print("❌ Erro! Digite um valor numérico válido.")
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

    # SUA SOLUÇÃO AQUI

    while True:
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para encerrar: ")
        
        if entrada.lower() == 'fim':
            break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
                continue
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número ou 'fim'.")
            continue
    
    if notas:
        total = len(notas)
        soma = sum(notas)
        media = soma / total
        maior = max(notas)
        menor = min(notas)
        
        print("\n" + "="*35)
        print("RELATÓRIO DA TURMA")
        print("="*35)
        print(f"Total de notas:    {total}")
        print(f"Média da turma:    {media:.2f}")
        print(f"Maior nota:        {maior}")
        print(f"Menor nota:        {menor}")
        print("="*35)
    else:
        print("❌ Nenhuma nota válida foi inserida.")
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

        # SUA SOLUÇÃO AQUI — leia a opção e implemente cada funcionalidade
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 0:
                print("✅ Saindo do sistema... Até mais!")
                break
            
            elif opcao == 1:
                try:
                    celsius = float(input("Digite a temperatura em °C: "))
                    fahrenheit = (celsius * 9/5) + 32
                    print(f"✅ {celsius}°C = {fahrenheit:.1f}°F")
                except ValueError:
                    print("❌ Erro! Digite um número válido.")
            
            elif opcao == 2:
                try:
                    n = int(input("Digite um número positivo: "))
                    if n <= 0:
                        print("❌ Digite um número positivo!")
                    elif n == 1:
                        print(f"❌ {n} não é primo.")
                    else:
                        primo = True
                        for i in range(2, int(n ** 0.5) + 1):
                            if n % i == 0:
                                primo = False
                                break
                        if primo:
                            print(f"✅ {n} é primo!")
                        else:
                            print(f"❌ {n} não é primo.")
                except ValueError:
                    print("❌ Erro! Digite um número inteiro.")
            
            elif opcao == 3:
                senha = input("Digite a senha: ")
                tamanho_ok = len(senha) >= 6
                tem_digito = any(c.isdigit() for c in senha)
                print(f"✓ Mínimo 6 caracteres: {'✅' if tamanho_ok else '❌'}")
                print(f"✓ Pelo menos 1 dígito:  {'✅' if tem_digito else '❌'}")
                if tamanho_ok and tem_digito:
                    print("✅ Senha válida!")
                else:
                    print("❌ Senha fraca!")
            
            elif opcao == 4:
                try:
                    num1 = float(input("Primeiro número: "))
                    num2 = float(input("Segundo número: "))
                    operacao = input("Operação (+, -, *, /): ")
                    
                    if operacao == "+":
                        resultado = num1 + num2
                        print(f"✅ {num1} + {num2} = {resultado:.2f}")
                    elif operacao == "-":
                        resultado = num1 - num2
                        print(f"✅ {num1} - {num2} = {resultado:.2f}")
                    elif operacao == "*":
                        resultado = num1 * num2
                        print(f"✅ {num1} × {num2} = {resultado:.2f}")
                    elif operacao == "/":
                        if num2 == 0:
                            print("❌ Erro: Divisão por zero!")
                        else:
                            resultado = num1 / num2
                            print(f"✅ {num1} ÷ {num2} = {resultado:.2f}")
                    else:
                        print("❌ Operação inválida! Use +, -, * ou /.")
                except ValueError:
                    print("❌ Erro! Digite números válidos.")
            
            else:
                print("❌ Opção inválida! Escolha 0, 1, 2, 3 ou 4.")
                
        except ValueError:
            print("❌ Erro! Digite um número inteiro para a opção.")
        pass


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): <Geandria de Menezes>")
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
