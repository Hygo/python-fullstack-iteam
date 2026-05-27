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
    pass  # ← apague esta linha e escreva seu código aqui


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
    # TODO: Remova espaços extras com .strip().
    #       Verifique se está vazia ou é igual a "sair".
    #       Use .split() para separar as palavras e confirme
    #       que o aluno informou ao menos 2 palavras.
    #       Retorne True apenas se todas as condições passarem.
    pass  # ← apague esta linha e escreva seu código aqui


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
    # TODO: Substitua vírgula por ponto para aceitar "7,5" como "7.5".
    #       Tente converter para float dentro de um bloco try/except.
    #       Se a conversão falhar (ValueError), retorne None.
    #       Se o número estiver fora do intervalo [0.0, 10.0], retorne None.
    #       Se tudo estiver correto, retorne o float convertido.
    pass  # ← apague esta linha e escreva seu código aqui
