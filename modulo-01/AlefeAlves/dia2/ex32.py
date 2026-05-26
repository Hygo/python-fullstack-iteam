from typing import Dict, List, Any

def validar_cadastro(dados: Dict[str, Any]) -> Dict[str, List[str]]:
    """Validar dados de cadastro de usuário.

    Args:
        dados (Dict[str, Any]): Dicionário com informações do usuário (nome, email, idade e cpf).
        nome ≥ 3 chars | email com @ e . | idade entre 18-120 | cpf com 11 dígitos numéricos.

    Returns: 
        Dict[str, List[str]]: Dicionário contendo lista de validações bem-sucedidas ou falhas.

    Example:
        >>> validar_cadastro({"nome": "João", "email": "joao@mail.com", "idade": 25, "cpf": "12345678901"})
        {'valido': ['nome', 'email', 'idade', 'cpf'], 'erros': []}   
    """
    valido: List[str] = []
    erros: List[str] = []

    nome = dados.get("nome", "")
    if isinstance(nome, str) and len(nome) >= 3:
        valido.append("nome")
    else:
        erros.append("Nome inválido: mínimo 2 caracteres")

    email = dados.get("email", "")
    if isinstance(email, str) and "@" in email and "." in email.split("@")[-1]:
        valido.append("email")
    else:
        erros.append("Email inválido: falta @ ou domínio")

    idade = dados.get("idade", 0)
    if isinstance(idade, int) and 18 <= idade <= 120:
        valido.append("idade")
    else:
        erros.append("Idade deve ser um inteiro entre 18 e 120")

    cpf = "".join(c for c in str(dados.get("cpf", "")) if c.isdigit())
    if len(cpf) == 11:
        valido.append("cpf")
    else:
        erros.append("CPF deve conter exatamente 11 dígitos numéricos")

    return {"valido": valido, "erros": erros}

user_valido = {"nome": "Álefe Alves", "email": "lefe@mail.com", "idade": 21, "cpf": "12345678901"}
user_invalido = {"nome": "aa", "email": "meuemail", "idade": 11, "cpf": "123a"}

print(f"Resultado para user válido:\n{validar_cadastro(user_valido)}")
print(f"Resulado para user inválido:\n{validar_cadastro(user_invalido)}")

print(validar_cadastro({"nome": "João", "email": "joao@mail.com", "idade": 25, "cpf": "12345678901"}))