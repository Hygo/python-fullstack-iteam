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
    # Remove espaços em branco
    nome_limpo = nome_turma.strip()
    # Verifica se está vazio ou igual a "sair"
    if not nome_limpo or nome_limpo.lower() == "sair":
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
    # Remove espaços em branco
    nome_limpo = nome_aluno.strip()
    # Verifica se está vazio ou igual a "sair"
    if not nome_limpo or nome_limpo.lower() == "sair":
        return False
    # Verifica se possui ao menos duas palavras
    if len(nome_limpo.split()) < 2:
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
    try:
        # Troca vírgula por ponto
        valor_limpo = str(valor_digitado).replace(",", ".")
        nota = float(valor_limpo)
        # Confere se a nota está no intervalo [0.0, 10.0]
        if 0.0 <= nota <= 10.0:
            return nota
        return None
    except ValueError:
        return None
