import json
import os

ARQUIVO = "contatos.json"

def _ler_arquivo() -> list:
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def _salvar_arquivo(contatos: list) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=2, ensure_ascii=False)


def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    """Adiciona um novo contato à agenda.

    Args:
        nome: Nome completo do contato.
        telefone: Número de telefone formatado.
        email: Endereço de e-mail do contato.
    """
    contatos = _ler_arquivo()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    _salvar_arquivo(contatos)


def listar_contatos() -> list:
    """Retorna todos os contatos da agenda.

    Returns:
        Lista de dicionários com nome, telefone e email.
    """
    return _ler_arquivo()


def buscar_contato(nome: str) -> dict | None:
    """Busca um contato pelo nome (busca parcial, sem distinção de maiúsculas).

    Args:
        nome: Nome ou parte do nome a pesquisar.

    Returns:
        Dicionário do primeiro contato encontrado ou None.
    """
    for contato in _ler_arquivo():
        if nome.lower() in contato["nome"].lower():
            return contato
    return None


def remover_contato(nome: str) -> bool:
    """Remove o primeiro contato que corresponda ao nome informado.

    Args:
        nome: Nome ou parte do nome a remover.

    Returns:
        True se o contato foi encontrado e removido, False caso contrário.
    """
    contatos = _ler_arquivo()
    novos = [c for c in contatos if nome.lower() not in c["nome"].lower()]
    if len(novos) == len(contatos):
        return False
    _salvar_arquivo(novos)
    return True


# Demonstração
if os.path.exists(ARQUIVO):
    os.remove(ARQUIVO)

adicionar_contato("Álefe Alves",  "(95) 99999-9999", "alefe@mail.com")
adicionar_contato("Amanda de Brito", "(95) 98888-8888", "amanda@mail.com")
adicionar_contato("Luciano dos Santos",   "(95) 97777-7777", "luciano@mail.com")

print("===== AGENDA DE CONTATOS =====")
for c in listar_contatos():
    print(f"  {c['nome']:<20} {c['telefone']}  {c['email']}")

print("\n--- Busca por 'Amanda' ---")
encontrado = buscar_contato("Amanda")
print(f"  Encontrado: {encontrado}")

print("\n--- Removendo 'Luciano' ---")
removido = remover_contato("Luciano")
print(f"  Removido: {removido}")

print("\n--- Agenda após remoção ---")
for c in listar_contatos():
    print(f"  {c['nome']:<20} {c['telefone']}")