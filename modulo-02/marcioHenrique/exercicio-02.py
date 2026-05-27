"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <Marcio Henrique>
Data    : <26/05/2026>
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
    
    pass
while True:
    try:
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        if temp_celsius < 0:
            print("❄️ Congelante")
        elif 0 <= temp_celsius <= 14:
            print("🥶 Frio")
        elif 15 <= temp_celsius <= 24:
            print("😊 Agradável")
        elif 25 <= temp_celsius <= 34:
            print("☀️ Quente")
        else:
            print("🔥 Muito quente")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a temperatura.")


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
    pass
while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == "admin":
        if senha == "iteam2025":
            print("Acesso concedido. Bem-vindo, admin!")
            break
        else:
            print("Senha incorreta. Tente novamente.")
    else:
        print("Usuário não encontrado. Tente novamente.")
        


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
while True:
    try:
        numero = int(input("Digite um número inteiro para ver sua tabuada: "))
        print(f"\nTabuada de {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero:2} x {i:2} = {resultado:3}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

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
while True:
    try:
        numero = int(input("Digite um número inteiro positivo para a contagem regressiva: "))
        if numero < 0:
            print("Por favor, digite um número inteiro positivo.")
            continue
        print("\nContagem regressiva:")
        while numero >= 0:
            print(f"{numero} ", end="")
            numero -= 1
        print("\n🚀 Lançamento!")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

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
for index, item in enumerate(estoque):
    if item == "Monitor":
        print(f"Item 'Monitor' encontrado na posição {index}.")
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
    pass
soma = 0
contador_validos = 0
contador_ignorados = 0
for leitura in leituras:
    if leitura is None:
        contador_ignorados += 1
        continue
    soma += leitura
    contador_validos += 1
media = soma / contador_validos if contador_validos > 0 else 0
print(f"Soma das leituras válidas: {soma:.2f}")
print(f"Média das leituras válidas: {media:.2f}")
print(f"Total de leituras ignoradas: {contador_ignorados}")


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
    pass    
while True:
    try:
        nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
        if 0.0 <= nota <= 10.0:
            if nota >= 9.0:
                conceito = "A – Excelente"
            elif nota >= 7.0:
                conceito = "B – Bom"
            elif nota >= 5.0:
                conceito = "C – Regular"
            else:
                conceito = "D – Insuficiente"
            print(f"Nota: {nota:.1f} → Conceito: {conceito}")
            break
        else:
            print("Nota inválida. Por favor, digite um valor entre 0.0 e 10.0.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a nota.")



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
    pass
input1 = input("Digite o primeiro número: ")
input2 = input("Digite o segundo número: ")
operacao = input("Digite a operação (+, -, *, /): ")
try:
    num1 = float(input1)
    num2 = float(input2)
    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2
    else:
        raise ValueError("Operação inválida. Use +, -, *, ou /.")
except ValueError as ve:
    print(f"Erro de valor: {ve}")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
else:
    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")
finally:
    print("Obrigado por usar a calculadora segura!")


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
    pass
print("Triângulo crescente:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
print("Triângulo decrescente:")
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
    pass
import random
numero_secreto = random.randint(1, 100)
tentativas = 7
print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 100. Você tem 7 tentativas.")
for tentativa in range(1, tentativas + 1):
    try:
        palpite = int(input(f"Tentativa {tentativa}: "))
        if palpite < numero_secreto:
            print("O número é maior. Tente novamente.")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativa} tentativas!")
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
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
    # SUA SOLUÇÃO AQUI
    pass
while True:
    try:
        numero = int(input("Digite um número inteiro positivo para verificar se é primo: "))
        if numero <= 1:
            print("Números menores ou iguais a 1 não são primos. Tente novamente.")
            continue
        if numero == 2:
            print("2 é um número primo.")
            break
        if numero % 2 == 0:
            print(f"{numero} não é um número primo (divisível por 2).")
            break
        primo = True
        for i in range(3, int(numero**0.5) + 1, 2):
            if numero % i == 0:
                print(f"{numero} não é um número primo (divisível por {i}).")
                primo = False
                break
        if primo:
            print(f"{numero} é um número primo.")
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro positivo.")


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
    pass
senha = input("Digite a senha para análise: ")
criterios = {
    "Mínimo 8 caracteres": len(senha) >= 8,
    "Pelo menos 1 maiúscula": any(c.isupper() for c in senha),
    "Pelo menos 1 minúscula": any(c.islower() for c in senha),
    "Pelo menos 1 dígito": any(c.isdigit() for c in senha),
    "Pelo menos 1 caractere especial": any(c in "!@#$%^&*" for c in senha)
}

print("Relatório de segurança da senha:")
for criterio, atendido in criterios.items():
    status = "✅" if atendido else "❌"
    print(f"{status} {criterio}")



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
    pass
while True:
    try:
        valor = int(input("Digite o valor do saque (múltiplo de R$10, máximo R$3.000): "))
        if valor <= 0 or valor > 3000 or valor % 10 != 0:
            print("Valor inválido. Por favor, digite um múltiplo de R$10 entre 1 e R$3.000.")
            continue
        print(f"Valor solicitado: R${valor}")
        for cedula in cedulas:
            quantidade = valor // cedula
            if quantidade > 0:
                print(f"{quantidade} cédula(s) de R${cedula}")
                valor -= quantidade * cedula
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para o valor do saque.")


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
    pass
while True:
    entrada = input("Digite a nota do aluno (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0.0 <= nota <= 10.0:
            notas.append(nota)
        else:
            print("Nota inválida. Por favor, digite um valor entre 0.0 e 10.0.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido para a nota ou 'fim' para encerrar.")
if notas:
    total = len(notas)
    media = sum(notas) / total
    maior = max(notas)
    menor = min(notas)
    print(f"\nTotal de notas: {total}")
    print(f"Média da turma: {media:.2f}")
    print(f"Maior nota: {maior:.2f}")
    print(f"Menor nota: {menor:.2f}")


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
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                ex01_classificador_temperatura()
            elif opcao == "2":
                ex11_numero_primo()
            elif opcao == "3":
                ex12_analisador_senha()
            elif opcao == "4":
                ex08_calculadora_segura()
            elif opcao == "0":
                print("Saindo do sistema. Até logo!")
                break  # ← sai do while True principal
            else:
                print("Opção inválida. Tente novamente.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}. Tente novamente.")
            

# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): <Marcio>")
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
