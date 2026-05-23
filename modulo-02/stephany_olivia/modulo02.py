"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <Stephany Olivia da Silva Pereira>
Data    : <23/05/2024>
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

# Lê a temperatura digitada pelo usuário e converte para número decimal
temperatura = float(input("Digite a temperatura em Celsius: "))

# Classifica a temperatura conforme a faixa
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

# Exibe o resultado
print(f"Temperatura: {temperatura:.0f}°C")
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
# Lê o usuário e a senha digitados
usuario = input("Usuário: ")
senha = input("Senha: ")

# Verifica primeiro o usuário, depois a senha
if usuario == "admin":
    if senha == "iteam2025":
        print("Acesso liberado. Bem-vindo!")
    else:
        print("Senha incorreta.")
else:
    print("Usuário não encontrado.")


# ==============================================================
# EXERCÍCIO 03 – Tabuada Interativa
# Conceitos: for, range(), f-string com alinhamento
# ==============================================================
def ex03_tabuada():
    """
    Solicita um número inteiro e exibe sua tabuada de 1 a 10.
    """
    # SUA SOLUÇÃO AQUI
# Lê o número digitado pelo usuário
numero = int(input("Digite um número para ver a tabuada: "))

print(f"\nTabuada do {numero}:")
print("-" * 20)

# Percorre de 1 a 10 e exibe a tabuada
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
numero = int(input("Digite um número para a contagem regressiva: "))

while numero >= 0:
    print(f"{numero}...", end=" ")
    numero -= 1  

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
estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]
encontrado = False

# Percorre a lista procurando o produto
for i in range(len(estoque)):
    if estoque[i] == "Monitor":
        encontrado = True
        print(f"✅ 'Monitor' encontrado na posição {i}!")
        break  # para o loop assim que achar

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
  leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]


soma = 0
total_validos = 0
total_ignorados = 0

for valor in leituras:
    if valor is None:
        total_ignorados += 1
        continue  # pula para o próximo sem executar o restante

    # Só chega aqui se o valor for válido
    soma += valor
    total_validos += 1

media = soma / total_validos
print(f"Soma dos válidos   : {soma:.1f}")
print(f"Média dos válidos  : {media:.2f}")
print(f"Registros ignorados: {total_ignorados}")


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
# Fica pedindo a nota até receber um valor válido
while True:
    nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))

    if 0.0 <= nota <= 10.0:
        break  # nota válida, sai do loop
    else:
        print("❌ Nota inválida! Digite um valor entre 0.0 e 10.0.")

# Classifica o conceito com base na nota válida
if nota >= 9.0:
    conceito = "A – Excelente"
elif nota >= 7.0:
    conceito = "B – Bom"
elif nota >= 5.0:
    conceito = "C – Regular"
else:
    conceito = "D – Insuficiente"

print(f"\nNota: {nota:.1f}")
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
    # Lê os dois números e a operação
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    # Verifica se a operação é válida
    if operacao not in ["+", "-", "*", "/"]:
        raise ValueError("Operação inválida.")

    # Realiza o cálculo conforme a operação escolhida
    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2

except ValueError as e:
    # Captura se o usuário digitou algo que não é número ou operação inválida
    print(f" Erro: {e}")

except ZeroDivisionError:
    # Captura se o usuário tentou dividir por zero
    print(" Erro: Não é possível dividir por zero.")

else:
    # Executado apenas se não houve nenhum erro
    print(f"\n Resultado: {numero1} {operacao} {numero2} = {resultado}")

finally:
    # Executado sempre, com ou sem erro
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
 # Triângulo crescente
for i in range(1, 6):        # linha 1 até 5
    for j in range(1, i + 1):  # coluna 1 até o número da linha
        print(j, end=" ")
    print()  # quebra a linha ao terminar cada fileira

print()  # espaço entre os triângulos

# Triângulo invertido (desafio extra)
for i in range(5, 0, -1):    # linha 5 até 1 (de trás pra frente)
    for j in range(1, i + 1):  # coluna 1 até o número da linha
        print(j, end=" ")
    print()  # quebra a linha ao terminar cada fileira


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
import random

# O computador escolhe um número secreto entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 7

print(" Adivinhe o número entre 1 e 100! Você tem 7 tentativas.")
print("-" * 45)

# Loop principal do jogo
while tentativas < max_tentativas:
    tentativas += 1
    chute = int(input(f"\nTentativa {tentativas}/{max_tentativas}: "))

    if chute == numero_secreto:
        print(f" Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print(" O número secreto é MAIOR.")
    else:
        print(" O número secreto é MENOR.")

    # Avisa quantas tentativas restam
    restantes = max_tentativas - tentativas
    if restantes > 0:
        print(f"   Tentativas restantes: {restantes}")

# Se esgotou todas as tentativas sem acertar
else:
    print(f"\n Game over! O número era {numero_secreto}.")


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
    numero = int(input("Digite um número inteiro positivo: "))

    # Não aceita números negativos ou zero
    if numero <= 0:
        raise ValueError("O número deve ser positivo.")

    # Casos especiais: 1 não é primo, 2 é primo
    if numero == 1:
        print(f"{numero} não é primo.")
    elif numero == 2:
        print(f"{numero}  é primo!")
    else:
        primo = True

        # Verifica divisores até a raiz quadrada do número
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                primo = False
                break  # achou um divisor, não precisa continuar

        if primo:
            print(f"{numero}  é primo!")
        else:
            print(f"{numero}  não é primo. (divisível por {i})")

except ValueError as e:
    print(f"❌ Entrada inválida: {e}")


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
senha = input("Digite uma senha para analisar: ")

# Variáveis booleanas para rastrear cada critério
tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False
especiais = "!@#$%^&*"

# Percorre cada caractere da senha verificando os critérios
for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True
    elif caractere.islower():
        tem_minuscula = True
    elif caractere.isdigit():
        tem_numero = True
    elif caractere in especiais:
        tem_especial = True

# Verifica o tamanho mínimo
tem_tamanho = len(senha) >= 8

# Exibe o relatório de cada critério
print("\n--- Relatório da Senha ---")
print(f"{'✅' if tem_tamanho   else '❌'} Mínimo 8 caracteres   (atual: {len(senha)})")
print(f"{'✅' if tem_maiuscula else '❌'} Letra maiúscula")
print(f"{'✅' if tem_minuscula else '❌'} Letra minúscula")
print(f"{'✅' if tem_numero    else '❌'} Número")
print(f"{'✅' if tem_especial  else '❌'} Caractere especial (!@#$%^&*)")

# Verifica se todos os critérios foram atendidos
todos_ok = all([tem_tamanho, tem_maiuscula, tem_minuscula, tem_numero, tem_especial])

print("-" * 30)
if todos_ok:
    print("🔒 Senha FORTE! Todos os critérios atendidos.")
else:
    print("⚠️  Senha FRACA! Corrija os critérios marcados com ❌.")


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
    valor = int(input("Digite o valor do saque (múltiplo de R$10, máximo R$3.000): R$ "))

    # Valida se o valor é válido
    if valor <= 0:
        print("❌ O valor deve ser positivo.")
    elif valor > 3000:
        print("❌ Valor máximo permitido é R$3.000.")
    elif valor % 10 != 0:
        print("❌ O valor deve ser múltiplo de R$10.")
    else:
        cedulas = [200, 100, 50, 20, 10]
        restante = valor
        i = 0  # controla qual cédula estamos usando

        print(f"\n💵 Saque de R${valor:.2f} — cédulas utilizadas:")
        print("-" * 35)

        # Percorre cada cédula enquanto ainda houver restante
        while restante > 0 and i < len(cedulas):
            cedula = cedulas[i]
            quantidade = restante // cedula  # quantas cédulas cabem

            if quantidade > 0:
                print(f"   R${cedula:>3}: {quantidade}x")
                restante -= cedula * quantidade  # desconta do restante

            i += 1  # passa para a próxima cédula

        print("-" * 35)
        print("✅ Saque realizado com sucesso!")

except ValueError:
    print("❌ Entrada inválida! Digite apenas números inteiros.")


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
notas = []  # lista que vai guardar as notas válidas

print("Digite as notas uma por uma. Quando terminar, digite 'fim'.")
print("-" * 50)

while True:
    entrada = input("Nota: ")

    # Encerra a leitura quando o usuário digitar 'fim'
    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)
    except ValueError:
        # Entrada não numérica — ignora e continua
        print("⚠️  Aviso: valor não numérico. Ignorado.")
        continue

    # Nota fora do intervalo — ignora e continua
    if nota < 0 or nota > 10:
        print("⚠️  Aviso: nota fora do intervalo (0 a 10). Ignorada.")
        continue

    # Nota válida — adiciona à lista
    notas.append(nota)
    print(f"✅ Nota {nota:.1f} registrada.")

# Exibe o relatório final
print("\n" + "=" * 50)
if len(notas) == 0:
    print("Nenhuma nota válida foi registrada.")
else:
    print(f"Total de notas válidas : {len(notas)}")
    print(f"Média                  : {sum(notas) / len(notas):.2f}")
    print(f"Maior nota             : {max(notas):.1f}")
    print(f"Menor nota             : {min(notas):.1f}")


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
# ─── Funções de cada opção do menu ───────────────────────

def conversor_temperatura():
    temp = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = temp * 9/5 + 32
    kelvin = temp + 273.15
    print(f"  Fahrenheit : {fahrenheit:.1f}°F")
    print(f"  Kelvin     : {kelvin:.2f}K")


def verificador_primo():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 2:
        print("  ❌ Não é primo.")
        return
    primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break
    print(f"  {'✅ É primo!' if primo else f'❌ Não é primo. (divisível por {i})'}")


def analisador_senha():
    senha = input("Digite uma senha: ")
    criterios = {
        "Mínimo 8 caracteres" : len(senha) >= 8,
        "Letra maiúscula"     : any(c.isupper() for c in senha),
        "Letra minúscula"     : any(c.islower() for c in senha),
        "Número"              : any(c.isdigit() for c in senha),
        "Caractere especial"  : any(c in "!@#$%^&*" for c in senha),
    }
    for criterio, ok in criterios.items():
        print(f"  {'✅' if ok else '❌'} {criterio}")
    print(f"  {'🔒 Senha FORTE!' if all(criterios.values()) else '⚠️  Senha FRACA!'}")


def calculadora_segura():
    a = float(input("  Primeiro número : "))
    b = float(input("  Segundo número  : "))
    op = input("  Operação (+,-,*,/): ")
    if op == "+":
        print(f"  Resultado: {a + b}")
    elif op == "-":
        print(f"  Resultado: {a - b}")
    elif op == "*":
        print(f"  Resultado: {a * b}")
    elif op == "/":
        if b == 0:
            print("  ❌ Não é possível dividir por zero.")
        else:
            print(f"  Resultado: {a / b:.2f}")
    else:
        print("  ❌ Operação inválida.")


# ─── Menu principal ───────────────────────────────────────

while True:

    # Exibe o menu
    print("\n=============================")
    print("   SISTEMA ITEAM - MENU     ")
    print("=============================")
    print("[1] Conversor de temperatura")
    print("[2] Verificador de número primo")
    print("[3] Analisador de senha")
    print("[4] Calculadora segura")
    print("[0] Sair")
    print("=============================")

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        # Entrada não numérica — avisa e volta ao menu
        print("⚠️  Opção inválida! Digite um número.")
        continue

    print()  # espaço visual antes do resultado

    if opcao == 0:
        print("👋 Encerrando o sistema. Até logo!")
        break
    elif opcao == 1:
        conversor_temperatura()
    elif opcao == 2:
        verificador_primo()
    elif opcao == 3:
        analisador_senha()
    elif opcao == 4:
        calculadora_segura()
    else:
        # Número válido mas fora das opções — ignora e continua
        print("⚠️  Opção não existe. Escolha entre 0 e 4.")
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
