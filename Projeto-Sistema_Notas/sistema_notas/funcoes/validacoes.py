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

    turma_limpa = nome_turma.strip() # Sem espaços 
    
    if turma_limpa == "" or turma_limpa.lower() == "sair":  # Se ficou vazio OU for igual a "sair" (independente de maiúsculas/minúsculas)
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

    aluno_limpo = nome_aluno.strip() 
    
    if aluno_limpo == "" or aluno_limpo.lower() == "sair": 
        return False
        
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

    valor_formatado = valor_digitado.replace(',', '.')
    
    try:
        nota = float(valor_formatado)
        
        #Verificação de intervalo 
        if 0.0 <= nota <= 10.0:
            return nota
        else:
            return None
            
    except ValueError:
        return None
