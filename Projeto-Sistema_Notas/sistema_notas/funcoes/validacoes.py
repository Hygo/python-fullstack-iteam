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
    # Remove espaços extras do início e fim
    turma_limpa = nome_turma.strip()

    # Verifica se está vazia ou se é igual a "sair" (usando .lower() para ser case-insensitive)
    if turma_limpa == "" or turma_limpa.lower() == "sair":
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
    # Remove espaços extras do início e fim
    aluno_limpo = nome_aluno.strip()

    # Verifica se está vazia ou se é igual a "sair"
    if aluno_limpo == "" or aluno_limpo.lower() == "sair":
        return False

    # Separa as palavras por espaços para contar quantas foram digitadas
    palavras = aluno_limpo.split()
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
    # Remove espaços e substitui a vírgula por ponto decimal
    valor_formatado = valor_digitado.strip().replace(",", ".")

    try:
        # Tenta a conversão para número decimal
        nota = float(valor_formatado)

        # Verifica se está dentro do intervalo permitido [0.0, 10.0]
        if nota < 0.0 or nota > 10.0:
            return None

        return nota

    except ValueError:
        # Retorna None caso o texto não seja um número válido (ex: "sete")
        return None
    