# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================


def validar_turma(nome_turma):
    """
    Valida o nome da turma informado pelo usuário.
    """
    nome = nome_turma.strip().lower()

    if nome == "" or nome == "sair":
        return False

    return True


def validar_aluno(nome_aluno):
    """
    Valida o nome do aluno informado pelo usuário.
    """
    nome = nome_aluno.strip()

    # Verifica vazio ou "sair"
    if nome == "" or nome.lower() == "sair":
        return False

    # Verifica se tem pelo menos nome e sobrenome
    partes = nome.split()
    if len(partes) < 2:
        return False

    return True


def validar_nota(valor_digitado):
    """
    Valida e converte uma nota digitada pelo usuário.
    """
    # Substitui vírgula por ponto
    valor_formatado = valor_digitado.replace(",", ".")

    try:
        nota = float(valor_formatado)
    except ValueError:
        return None

    # Verifica intervalo válido
    if nota < 0.0 or nota > 10.0:
        return None

    return nota