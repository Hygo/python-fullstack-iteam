import json
from typing import List, Dict, Optional

ARQUIVO = "contatos.json"


def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    """
    Adiciona um contato à agenda.

    Args:
        nome (str): Nome do contato.
        telefone (str): Telefone do contato.
        email (str): Email do contato.

    Returns:
        None
    """
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            contatos = json.load(f)
    except FileNotFoundError:
        contatos = []

    contatos.append({"nome": nome, "telefone": telefone, "email": email})

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=2, ensure_ascii=False)


def listar_contatos() -> List[Dict[str, str]]:
    """
    Lista todos os contatos da agenda.

    Returns:
        List[Dict[str, str]]: Lista de contatos.
    """
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def buscar_contato(nome: str) -> Optional[Dict[str, str]]:
    """
    Busca um contato pelo nome.

    Args:
        nome (str): Nome do contato a ser buscado.

    Returns:
        Optional[Dict[str, str]]: Contato encontrado ou None.
    """
    contatos = listar_contatos()
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            return contato
    return None


def remover_contato(nome: str) -> bool:
    """
    Remove um contato pelo nome.

    Args:
        nome (str): Nome do contato a ser removido.

    Returns:
        bool: True se o contato foi removido, False caso contrário.
    """
    contatos = listar_contatos()
    novos_contatos = [c for c in contatos if c["nome"].lower() != nome.lower()]

    if len(novos_contatos) == len(contatos):
        return False  # não encontrou

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(novos_contatos, f, indent=2, ensure_ascii=False)
    return True


# --- Demonstração ---
print("--- Agenda de Contatos ---")

# 1. Adicionar 3 contatos
adicionar_contato("Alice", "55999999999", "alice@email.com")
adicionar_contato("Bruno", "55888888888", "bruno@email.com")
adicionar_contato("Carla", "55777777777", "carla@email.com")

# 2. Listar contatos
print("\nLista de contatos:")
for c in listar_contatos():
    print(f"{c['nome']} - {c['telefone']} - {c['email']}")

# 3. Buscar um contato
print("\nBuscando contato 'Bruno':")
print(buscar_contato("Bruno"))

# 4. Remover um contato
print("\nRemovendo contato 'Alice':")
print("Removido?" , remover_contato("Alice"))

print("\nLista atualizada:")
for c in listar_contatos():
    print(f"{c['nome']} - {c['telefone']} - {c['email']}")
