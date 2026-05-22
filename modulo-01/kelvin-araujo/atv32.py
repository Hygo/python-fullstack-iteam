### 🔴 Exercício 32 – Validador de Cadastro com Typing
# Função validar_cadastro com type hints e docstring completa.
# Regras: nome ≥ 3 chars | email com @ e . | idade 18-120 | cpf com 11 dígitos numéricos.

from typing import Dict, List, Any


def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """Valida os dados de cadastro de um usuário.

    Args:
        dados: Dicionário com os campos nome, email, idade e cpf.

    Returns:
        Dicionário com chaves "valido" (campos aprovados) e "erros" (mensagens de falha).

    Example:
        >>> resultado = validar_cadastro({"nome": "Ana", "email": "ana@mail.com", "idade": 25, "cpf": "12345678901"})
        >>> resultado["erros"]
        []
    """
    valido: List[str] = []
    erros: List[str] = []

    nome = dados.get("nome", "")
    if isinstance(nome, str) and len(nome) >= 3:
        valido.append("nome")
    else:
        erros.append("nome deve ter pelo menos 3 caracteres")

    email = dados.get("email", "")
    if isinstance(email, str) and "@" in email and "." in email.split("@")[-1]:
        valido.append("email")
    else:
        erros.append("email inválido (deve conter '@' e '.' após o domínio)")

    idade = dados.get("idade", 0)
    if isinstance(idade, int) and 18 <= idade <= 120:
        valido.append("idade")
    else:
        erros.append("idade deve ser um inteiro entre 18 e 120")

    cpf = str(dados.get("cpf", ""))
    if cpf.isdigit() and len(cpf) == 11:
        valido.append("cpf")
    else:
        erros.append("cpf deve conter exatamente 11 dígitos numéricos")

    return {"valido": valido, "erros": erros}


cadastro_ok = {"nome": "Kelvin Araújo", "email": "kelvin@empresa.com", "idade": 25, "cpf": "12345678901"}
cadastro_ruim = {"nome": "Jo", "email": "emailsemarroba", "idade": 15, "cpf": "123"}

for rotulo, dados in [("Válido", cadastro_ok), ("Inválido", cadastro_ruim)]:
    resultado = validar_cadastro(dados)
    print(f"\n--- Cadastro {rotulo} ---")
    print(f"Campos aprovados : {resultado['valido']}")
    print(f"Erros encontrados: {resultado['erros']}")
