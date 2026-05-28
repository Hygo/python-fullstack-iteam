# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================


def validar_turma(nome_turma):
    """
    Valida o nome da turma informado pelo usuário.

    Regras:
        - Não pode ser uma string vazia ou só espaços
        - Não pode ser igual a "sair" (palavra reservada para encerrar)

    Parâmetros:
        nome_turma (str): valor digitado pelo usuário

    Retorno:
        bool: True se válido, False caso contrário
    """
    # TODO: Verifique se nome_turma, após remover espaços com .strip(),
    #       está vazia OU é igual à palavra "sair" (case-insensitive).
    #       Se qualquer uma das condições for verdadeira, retorne False.
    #       Caso contrário, retorne True.
    if nome_turma.strip().lower()== "sair" or  not nome_turma.strip():
         return False
    else:
        return True


def validar_aluno(nome_aluno):
    """
    Valida o nome do aluno informado pelo usuário.

    Regras:
        - Não pode ser uma string vazia ou só espaços
        - Não pode ser igual a "sair"
        - Deve conter ao menos duas palavras
    """

    # remove espaços extras
    nome_aluno = nome_aluno.strip()

    # verifica vazio
    if nome_aluno == "":
        return False

    # verifica "sair"
    if nome_aluno.lower() == "sair":
        return False

    # separa as palavras
    palavras = nome_aluno.split()

    # precisa ter nome e sobrenome
    if len(palavras) < 2:
        return False

    return True


def validar_nota(valor_digitado):
    """
    Valida e converte uma nota digitada pelo usuário.

    Regras:
        - Deve ser um número
        - Deve estar entre 0 e 10
    """

    # aceita vírgula
    valor_digitado = valor_digitado.replace(",", ".")

    try:
        nota = float(valor_digitado)

    except ValueError:
        return None

    # valida intervalo
    if nota < 0 or nota > 10:
        return None

    return nota