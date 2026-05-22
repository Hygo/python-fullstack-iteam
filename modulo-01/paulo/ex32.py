from typing import Dict, List, Any

def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """
    Valida um dicionário de dados de cadastro.

    Args:
        dados (Dict[str, Any]): Dicionário com dados do cadastro.

    Returns:
        Dict[str, List[str]]: Resultado contendo listas de campos válidos e erros.
    """
    resultado: Dict[str, List[str]] = {"valido": [], "erros": []}

    nome = dados.get("nome", "")
    if isinstance(nome, str) and len(nome) >= 3:
        resultado["valido"].append("nome")
    else:
        resultado["erros"].append("Nome inválido (deve ter >= 3 caracteres)")

    email = dados.get("email", "")
    if isinstance(email, str) and "@" in email and "." in email:
        resultado["valido"].append("email")
    else:
        resultado["erros"].append("E-mail inválido")

    idade = dados.get("idade", 0)
    if isinstance(idade, (int, float)) and 18 <= idade <= 120:
        resultado["valido"].append("idade")
    else:
        resultado["erros"].append("Idade inválida (entre 18 e 120)")

    cpf = dados.get("cpf", "")
    if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
        resultado["valido"].append("cpf")
    else:
        resultado["erros"].append("CPF inválido (11 dígitos numéricos)")

    return resultado

validos = {"nome": "Ana", "email": "ana@teste.com", "idade": 25, "cpf": "12345678901"}
invalidos = {"nome": "Z", "email": "anateste.com", "idade": 15, "cpf": "123"}

print("Válidos:", validar_cadastro(validos))
print("Inválidos:", validar_cadastro(invalidos))
