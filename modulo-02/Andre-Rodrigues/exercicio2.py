"""
=============================================================
MÓDULO 2 – Estruturas de Controle
Curso de Capacitação Full Stack – ITEAM

Aluno(a): <ANDRE DA SILVA RODRIGUES>
Data    : <22/05/2026>
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

    
    temperatura = float(input("Temperatura em °C: "))
    
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
        
    print(f"Temperatura: {temperatura}°C")
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

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "iteam2025"

usuario_digitado = input("Usuário: ")

if usuario_digitado == USUARIO_CORRETO:
    senha_digitada = input("Senha: ")
    
    if senha_digitada == SENHA_CORRETA:
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

    numero = int(input("Digite um número inteiro para ver a tabuada: "))
    
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

    num = int(input("Digite um número inteiro positivo para a contagem: "))
    
    if num < 0:
        print("Por favor, digite um número positivo.")
    else:
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

    # SUA SOLUÇÃO AQUI

estoque = ["Teclado", "Mouse", "Webcam", "Monitor", "Headset", "Notebook"]

produto_procurado = "Monitor"
encontrado = False

for posicao, produto in enumerate(estoque):
    if produto == produto_procurado:
        print(f"Produto '{produto_procurado}' encontrado na posição {posicao} do estoque.")
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

   
leituras = [12.5, None, 8.3, None, 15.0, 9.7, None, 11.2, 6.8, None]
valores_validos = [v for v in leituras if v is not None]

soma = sum(valores_validos)                 
media = soma / len(valores_validos)          

ignorados = len(leituras) - len(valores_validos)

print(f"Soma dos valores válidos: {soma:.1f}")
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
    # SUA SOLUÇÃO AQUI

while True:
    nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))
    if 0.0 <= nota <= 10.0:
        break
    print("Nota inválida. Tente novamente.")

if nota >= 9.0:
    conceito = "A - Excelente"
elif nota >= 7.0:
    conceito = "B - Bom"
elif nota >= 5.0:
    conceito = "C - Regular"
else:
    conceito = "D - Insuficiente"

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
    # SUA SOLUÇÃO AQUI]

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ").strip()

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        resultado = num1 / num2  
    else:
        raise ValueError("Operação inválida.")

except ValueError as erro:
    if "Operação inválida" in str(erro):
        print("Erro: Operação inválida! Use apenas +, -, * ou /.")
    else:
        print("Erro: Digite apenas valores numéricos válidos.")

except ZeroDivisionError:
    print("Erro: Não é possível dividir um número por zero.")

else:
    print(f"✅ Resultado: {num1} {operacao} {num2} = {resultado}")

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
     for j in range(1, i + 1):
        print(j, end=" ")
    print()

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
    """
    O computador sorteia um número entre 1 e 100.
    O usuário tem 7 tentativas para adivinhar.
    A cada erro, indica se o número é maior ou menor.
    """
    import random
    numero_secreto = random.randint(1, 100)

    # SUA SOLUÇÃO AQUI


import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 7

while tentativas < max_tentativas:
    tentativas += 1
    chute = int(input(f"Tentativa {tentativas}/{max_tentativas}: "))

    if chute == numero_secreto:
        print(f" Parabéns! Você acertou em {tentativas} tentativas.")
        break
    elif chute < numero_secreto:
        print(" O número secreto é maior.")
    else:
        print(" O número secreto é menor.")
else:
    print(f" Game over! O número era {numero_secreto}.")


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

def nprimo(n):
    if n < 2:
        return False, None
    if n == 2:
        return True, None
    if n % 2 == 0:
        return False, 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False, i
    return True, None


while True:
    try:
        n = int(input("Digite um número inteiro positivo (0 para sair): "))
        if n == 0:
            print("Encerrando...")
            break

        primo, divisor = nprimo(n)

        if primo:
            print(f" {n} é um número primo.")
        else:
            print(f" {n} não é primo. Divisível por {divisor}.")

    except ValueError:
        print(" Digite apenas números inteiros.")


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

senha = input("Digite a senha: ")
especiais = "!@#$%^&*"

tem_maiuscula  = False
tem_minuscula  = False
tem_numero     = False
tem_especial   = False

for c in senha:
    if c.isupper():
        tem_maiuscula = True
    elif c.islower():
        tem_minuscula = True
    elif c.isdigit():
        tem_numero = True
    elif c in especiais:
        tem_especial = True

comprimento_ok = len(senha) >= 8

print(f"\nAnalisando: {senha}")
print(f"{'✅' if comprimento_ok else '❌'} Comprimento adequado ({len(senha)} caracteres)")
print(f"{'✅' if tem_maiuscula  else '❌'} Contém maiúscula")
print(f"{'✅' if tem_minuscula  else '❌'} Contém minúscula")
print(f"{'✅' if tem_numero     else '❌'} Contém número")
print(f"{'✅' if tem_especial   else '❌'} Contém caractere especial")

if all([comprimento_ok, tem_maiuscula, tem_minuscula, tem_numero, tem_especial]):
    print("Senha FORTE!")
else:
    print("Senha FRACA. Melhore os critérios acima.")


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
    
    cedulas = [200, 100, 50, 20, 10]

    while True:
        try:
            entrada = input("Digite o valor do saque (ou 'sair'): ").strip()
            if entrada.lower() == 'sair':
                print("Operação cancelada.")
                break

            valor = int(entrada)

            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            if valor > 3000:
                print("Limite máximo de saque é de R$ 3.000.")
                continue
            if valor % 10 != 0:
                print(" Valor inválido. Este caixa possui apenas notas de R$ 200, 100, 50, 20 e 10.")
                continue

            print(f"Dispensando R$ {valor}:")
            
            for nota in cedulas: qtd_notas = valor // nota
                
            
            if qtd_notas > 0:
                    print(f"  -> {qtd_notas} nota(s) de R$ {nota}")
                    valor = valor % nota 

            print("Saque finalizado com sucesso!\n")
            break

        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")


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

notas = []

while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")

    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)
    except ValueError:
        print(" Entrada inválida, ignorada.")
        continue

    if not 0 <= nota <= 10:
        print(" Nota fora do intervalo (0-10), ignorada.")
        continue

    notas.append(nota)

if notas:
    print(f"\nNotas válidas:  {len(notas)}")
    print(f"Média:          {sum(notas)/len(notas):.2f}")
    print(f"Maior nota:     {max(notas)}")
    print(f"Menor nota:     {min(notas)}")
else:
    print("Nenhuma nota válida registrada.")


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
        

while True:
        print("   SISTEMA ITEAM - MENU    ")
        print("[1] Conversor de temperatura")
        print("[2] Verificador de número primo")
        print("[3] Analisador de senha")
        print("[4] Calculadora segura")
        print("[0] Sair")

        opcao = input("Escolha uma opção: ").strip()

        # Saida do Sistema
        if opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break

        # Conversor de Temperatura
        elif opcao == "1":
            print("Conversor: Celsius - Fahrenheit")
            try:
                celsius = float(input("Digite a temperatura em °C: "))
                fahrenheit = (celsius * 9 / 5) + 32
                print(f"{celsius}°C equivalem a {fahrenheit:.1f}°F")
            except ValueError:
                print("Erro: Por favor, digite um número válido para a temperatura.")

        # Verificador Numero Primo
        elif opcao == "2":
            print("Verificador de Número Primo")
            try:
                num = int(input("Digite um número inteiro positivo: "))
                if num <= 1:
                    print(f"{num} não é um número primo.")
                else:
                    ePrimo = True
                    for i in range(2, num):
                        if num % i == 0:
                            ePrimo = False
                            break
                    
                    if ePrimo:
                        print(f"{num} é um número primo!")
                    else:
                        print(f"{num} NÃO é um número primo.")
            except ValueError:
                print("Erro: Digite apenas números inteiros.")

        # Analisando a Senha
        elif opcao == "3":
            print("Analisador de Senha")
            senha = input("Digite a senha para análise: ")
            
            # Regras
            tamanho_ok = len(senha) >= 6
            tem_digito = any(char.isdigit() for char in senha)

            if tamanho_ok and tem_digito:
                print("Senha aprovada! Atende aos critérios de segurança.")
            else:
                print("Senha fraca. Motivos:")
                if not tamanho_ok:
                    print("  - Deve ter no mínimo 6 caracteres.")
                if not tem_digito:
                    print("  - Deve conter pelo menos um número.")

        # Calculadora
        elif opcao == "4":
            print("Calculadora Segura")
            try:
                num1 = float(input("Digite o primeiro número: "))
                operador = input("Digite o operador (+, -, *, /): ").strip()
                num2 = float(input("Digite o segundo número: "))

                if operador == "+":
                    print(f"Resultados: {num1} + {num2} = {num1 + num2}")
                elif operador == "-":
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif operador == "*":
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif operador == "/":
                    if num2 == 0:
                        print("Erro: Não é possível dividir por zero.")
                    else:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Operador inválido! Use apenas +, -, * ou /.")
            except ValueError:
                print("Erro: Entrada inválida. Digite números válidos.")

        else:
            print(" Opção inválida! Escolha um número de 0 a 4.")
            continue






# ==============================================================
# EXECUÇÃO PRINCIPAL
# Descomente as chamadas dos exercícios que você já resolveu.
# ==============================================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("MÓDULO 2 – Estruturas de Controle")
    print(f"Aluno(a): ANDRE DA SILVA RODRIGUES")
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
