# ============================================================
# MÓDULO: validacoes.py
# Responsável por todas as funções de validação do sistema
# ============================================================


def checar_sair(valor: str) -> bool:
    """Retorna True se o usuário digitou 'sair' (independente de maiúsculas/minúsculas)."""
    return valor.strip().lower() == 'sair'

def validar_turma(nome_turma: str) -> bool:
    """Valida se o nome da turma não é vazio."""
    return bool(nome_turma.strip())

def validar_aluno(nome_aluno: str) -> bool:
    """Valida se o aluno tem pelo menos nome e sobrenome (2 palavras)."""
    palavras = nome_aluno.strip().split()
    return len(palavras) >= 2

def validar_nota(nota_str: str) -> float | None:
    """
    Substitui vírgula por ponto, tenta converter para float e 
    valida se está entre 0.0 e 10.0. Retorna o float se válido, ou None se inválido.
    """
    try:
        # Trata o uso de vírgula como separador decimal
        nota_limpa = nota_str.replace(',', '.')
        nota_float = float(nota_limpa)
        if 0.0 <= nota_float <= 10.0:
            return nota_float
        return None
    except ValueError:
        return None