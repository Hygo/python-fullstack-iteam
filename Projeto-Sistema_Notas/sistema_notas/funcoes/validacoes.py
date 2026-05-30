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
    turma = nome_turma.strip()
    if turma == "" or turma.lower() == "sair":
        return False
    return True


def validar_aluno(nome_aluno):
    """
    Valida o nome do aluno informado pelo usuário.

    Regras:
        - Não pode ser uma string vazia ou só espaços
        - Não pode ser igual a "sair"
        - Deve conter ao menos duas palavras (nome e sobrenome)

    Parâmetros:
        nome_aluno (str): valor digitado pelo usuário

    Retorno:
        bool: True se válido, False caso contrário
    """
    aluno = nome_aluno.strip()
    if aluno == "" or aluno.lower() == "sair":
        return False

    palavras = aluno.split()
    if len(palavras) < 2:
        return False

    return True


def validar_nota(valor_digitado):
    """
    Valida e converte uma nota digitada pelo usuário.

    Regras:
        - Deve ser um número (aceita ponto ou vírgula como decimal)
        - Deve estar entre 0.0 e 10.0 (inclusive)

    Parâmetros:
        valor_digitado (str): string digitada pelo usuário

    Retorno:
        float ou None: o valor convertido se válido, ou None se inválido
    """
    valor_normalizado = valor_digitado.strip().replace(",", ".")
    try:
        nota = float(valor_normalizado)
    except ValueError:
        return None

    if nota < 0.0 or nota > 10.0:
        return None

    return nota
