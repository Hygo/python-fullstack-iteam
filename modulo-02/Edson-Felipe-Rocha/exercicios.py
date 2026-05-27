"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): EDSON FELIPE ROCHA CONSTANCIO
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
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "iteam2025":
        print("Acesso concedido.")
    else:
        print("Acesso negado.")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    numero = int(input("Digite um número inteiro para ver sua tabuada: "))
    print(f"\nTabuada de {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero:2} x {i:2} = {resultado:3}")
    


# ==============================================================
# EXERCÍCIO 04 – Contador Regressivo
# Conceitos: while, print com end=
# ==============================================================
def ex04_contador_regressivo():
    """
    Solicita um número inteiro positivo e faz a contagem
    regressiva até 0, finalizando com '🚀 Lançamento!'.
    """
    numero = int(input("Digite um número inteiro positivo para contagem regressiva: "))
    for i in range(numero, -1, -1):
        print(i, end=" ") 
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

    item_desejado = input('Digite o item que deseja buscar no estoque: ')
    for i, item in enumerate(estoque):
        if item == item_desejado:
            print(f"Item encontrado na posição {i}.")
            break
    else:
        print("Item não encontrado no estoque.")


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
    total_ignorados = 0

    for leitura in leituras:
        if leitura is None:
            total_ignorados += 1
            continue
        soma += leitura

    quantidade_validas = len(leituras) - total_ignorados
    media = soma / quantidade_validas if quantidade_validas > 0 else 0.0

    print(f"Soma: {soma:.1f}")
    print(f"Média: {media:.1f}")
    print(f"Total ignorados: {total_ignorados}")


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
    nota_aluno = float(input("Digite a nota do aluno (0.0 a 10.0): "))
    while True:
        if 0.0 <= nota_aluno <= 10.0:
            if nota_aluno >= 9.0:
                conceito = "A – Excelente"
            elif nota_aluno >= 7.0:
                conceito = "B – Bom"
            elif nota_aluno >= 5.0:
                conceito = "C – Regular"
            else:
                conceito = "D – Insuficiente"
            print(f"Nota válida: {nota_aluno:.1f} → Conceito: {conceito}")
            break
        else:
            print("Nota inválida! Digite um valor entre 0.0 e 10.0.")
            nota_aluno = float(input("Digite a nota do aluno (0.0 a 10.0): "))


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
        number1 = float(input("Digite o primeiro número: "))
        number2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: Entrada inválida! Certifique-se de digitar números válidos.")
        return

    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        if operacao == '+':
            resultado = number1 + number2
        elif operacao == '-':
            resultado = number1 - number2
        elif operacao == '*':
            resultado = number1 * number2
        elif operacao == '/':
            if number2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                return
            resultado = number1 / number2
        else:
            print("Operação inválida! Por favor, use +, -, * ou /.")
            return
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return
    else:
        print(f"Resultado: {resultado}")
    finally:
        print("Operação finalizada.")



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
        print()  # Nova linha após cada linha do triângulo crescente

    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()  # Nova linha após cada linha do triângulo decrescente


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
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100. Você tem 7 tentativas.")     
    input("Pressione Enter para começar...") # Pausa para o usuário se preparar
    tentativa = int(input("Escolha um número entre 1 e 100: "))
    while tentativas > 0:
            if tentativa < numero_secreto:
                print("O número é maior! Tente novamente.")
            elif tentativa > numero_secreto:
                print("O número é menor! Tente novamente.")
            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto}!")
                break
            tentativas -= 1
            if tentativas > 0:
                tentativa = int(input(f"Você tem {tentativas} tentativas restantes. Escolha outro número: "))
            else:
                print(f"Suas tentativas acabaram! O número secreto era {numero_secreto}.")


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
    n = int(input("Digite um número inteiro positivo para verificar se é primo: "))
    if n <= 1:
        print("Números menores ou iguais a 1 não são primos.")
        return
    for i in range  (2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} não é primo. Divisível por {i}.")
            break
    else:
        print(f"{n} é primo.")  


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
    print("Analisador de Senha Forte")
    print("Deve ter pelo menos 8 caracteres, 1 maiúscula, 1 minúscula, 1 dígito e 1 caractere especial (!@#$%^&*)")
    senha = input("Digite a senha para análise: ")
    tem_minuscula = any(c.islower() for c in senha)
    tem_maiuscula = any(c.isupper() for c in senha) 
    tem_digito = any(c.isdigit() for c in senha)
    tem_especial = any(c in "!@#$%^&*" for c in senha)

    print("\nRelatório de Segurança da Senha:")
    print(f"✅ Mínimo 8 caracteres: {'Sim' if len(senha) >= 8 else 'Não'}")
    print(f"✅ Pelo menos 1 maiúscula: {'Sim' if tem_maiuscula else 'Não'}")
    print(f"✅ Pelo menos 1 minúscula: {'Sim' if tem_minuscula else 'Não'}")
    print(f"✅ Pelo menos 1 dígito: {'Sim' if tem_digito else 'Não'}")
    print(f"✅ Pelo menos 1 caractere especial: {'Sim' if tem_especial else 'Não'}")
    print("\nSenha forte!" if all([len(senha) >= 8, tem_maiuscula, tem_minuscula, tem_digito, tem_especial]) else "Senha fraca! Considere melhorar os critérios não atendidos.")


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

    valor = float(input("Digite o valor do saque (múltiplo de R$10, máximo R$3.000): "))
    if valor <= 0 or valor > 3000 or valor % 10 != 0:
        print("Valor inválido! O valor deve ser um múltiplo de R$10 e não pode exceder R$3.000.")
        return
    print(f"\nSaque solicitado: R${valor:.2f}")
    print("Cédulas a serem entregues:")     
    for cedula in cedulas:
        quantidade = int(valor // cedula)
        if quantidade > 0:
            print(f"{quantidade} cédula(s) de R${cedula}")
            valor -= quantidade * cedula
        
  


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
        # 1. Pede a entrada como texto (string) primeiro
        entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

        # 2. Verifica a condição de parada antes de converter para número
        if entrada.lower() == 'fim':
            print("Encerrando a leitura de notas...")
            break
        
        # 3. Tenta converter a entrada para float (número decimal)
        try:
            nota = float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número ou a palavra 'fim'.")
            continue # Volta para o início do loop

        # 4. Verifica se a nota está no intervalo permitido
        if nota < 0 or nota > 10: 
            print("Nota inválida! A nota deve ser entre 0 e 10.")
            continue
        
        # 5. Se passou por todas as verificações, adiciona à lista
        notas.append(nota)
        print("Nota válida! Adicionada à lista.\n")

    # 6. Exibe o resumo final (apenas se pelo menos uma nota foi digitada)
    if len(notas) > 0:
        total = len(notas) # Quantidade de notas lidas
        media = sum(notas) / total
        maior_nota = max(notas)
        menor_nota = min(notas) 
        
        print("\n--- Resumo da Turma ---")
        print(f"Total de notas lidas: {total}")
        print(f"Média da turma: {media:.2f}")
        print(f"Maior nota: {maior_nota}")
        print(f"Menor nota: {menor_nota}")
    else:
        print("\nNenhuma nota válida foi inserida.")



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

        escolha = input("Escolha uma opção: ")
        try:
            opcao = int(escolha)    
        except ValueError:
            print("Entrada inválida! Por favor, digite um número correspondente às opções.")
            continue
        if opcao == 1:
            ex01_classificador_temperatura()
        elif opcao == 2:
            ex11_numero_primo()
        elif opcao == 3:
            ex12_analisador_senha()
        elif opcao == 4:
            ex08_calculadora_segura()
        elif opcao == 0:
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção do menu.")    
            print("Sistema encerrado.")   


# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): EDSON FELIPE ROCHA CONSTANCIO")
    print("=" * 50)

    # Descomente linha por linha conforme for resolvendo:
    #ex01_classificador_temperatura()
    #ex02_validador_acesso()
    #ex03_tabuada()
    #ex04_contador_regressivo()
    #ex05_buscador_break()
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