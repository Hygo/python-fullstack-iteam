from typing import Dict, List, Any

def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Valida os dados de cadastro de um usuário.

    Args:
        dados (Dict[str, Any]): Dicionário contendo os campos do cadastro.
            Campos esperados:
            - nome (str): Nome do usuário, mínimo 3 caracteres.
            - email (str): Deve conter '@' e '.'.
            - idade (int): Deve estar entre 18 e 120 anos.
            - cpf (str): Deve conter exatamente 11 dígitos numéricos.

    Returns:
        Dict[str, List[str]]: Dicionário com duas listas:
            - "valido": Lista de campos válidos.
            - "erros": Lista de mensagens de erro para campos inválidos.

    Example:
        >>> validar_cadastro({"nome": "Ana", "email": "ana@email.com", "idade": 25, "cpf": "12345678901"})
        {'valido': ['nome', 'email', 'idade', 'cpf'], 'erros': []}

        >>> validar_cadastro({"nome": "Jo", "email": "joemail.com", "idade": 15, "cpf": "123"})
        {'valido': [], 'erros': ['Nome deve ter pelo menos 3 caracteres.',
                                 'Email inválido.',
                                 'Idade deve estar entre 18 e 120.',
                                 'CPF deve conter 11 dígitos numéricos.']}
    """
    resultado = {"valido": [], "erros": []}

    # Validação do nome
    if isinstance(dados.get("nome"), str) and len(dados["nome"]) >= 3:
        resultado["valido"].append("nome")
    else:
        resultado["erros"].append("Nome deve ter pelo menos 3 caracteres.")

    # Validação do email
    email = dados.get("email", "")
    if isinstance(email, str) and "@" in email and "." in email:
        resultado["valido"].append("email")
    else:
        resultado["erros"].append("Email inválido.")

    # Validação da idade
    idade = dados.get("idade")
    if isinstance(idade, int) and 18 <= idade <= 120:
        resultado["valido"].append("idade")
    else:
        resultado["erros"].append("Idade deve estar entre 18 e 120.")

    # Validação do CPF
    cpf = dados.get("cpf", "")
    if isinstance(cpf, str) and cpf.isdigit() and len(cpf) == 11:
        resultado["valido"].append("cpf")
    else:
        resultado["erros"].append("CPF deve conter 11 dígitos numéricos.")

    return resultado


# Testando com dados válidos
dados_validos = {"nome": "Ana", "email": "ana@email.com", "idade": 25, "cpf": "12345678901"}
print(validar_cadastro(dados_validos))

# Testando com dados inválidos
dados_invalidos = {"nome": "Jo", "email": "joemail.com", "idade": 15, "cpf": "123"}
print(validar_cadastro(dados_invalidos))
