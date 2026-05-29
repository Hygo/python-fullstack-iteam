# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================


def validar_turma(nome_turma):
    turma = nome_turma.strip()

    if not turma or turma.lower() == "sair":
        return False

    return True


def validar_aluno(nome_aluno):
    aluno = nome_aluno.strip()

    if not aluno or aluno.lower() == "sair":
        return False

    if len(aluno.split()) < 2:
        return False

    return True


def validar_nota(valor_digitado):
    valor_normalizado = valor_digitado.replace(",", ".")

    try:
        nota = float(valor_normalizado)
    except ValueError:
        return None

    if nota < 0.0 or nota > 10.0:
        return None

    return nota