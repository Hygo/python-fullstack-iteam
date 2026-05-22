import json
import os

ARQUIVO = "contatos.json"

def carregar_contatos() -> list:
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_contatos(contatos: list) -> None:
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4)

def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    contatos = carregar_contatos()
    contatos.append({"nome": nome, "telefone": telefone, "email": email})
    salvar_contatos(contatos)

def listar_contatos() -> list:
    return carregar_contatos()

def buscar_contato(nome: str) -> dict | None:
    for contato in carregar_contatos():
        if contato["nome"].lower() == nome.lower():
            return contato
    return None

def remover_contato(nome: str) -> bool:
    contatos = carregar_contatos()
    for i, contato in enumerate(contatos):
        if contato["nome"].lower() == nome.lower():
            del contatos[i]
            salvar_contatos(contatos)
            return True
    return False

# Limpa o arquivo para demonstração
if os.path.exists(ARQUIVO):
    os.remove(ARQUIVO)

# Demonstração
adicionar_contato("Ana", "11999999999", "ana@email.com")
adicionar_contato("Carlos", "11888888888", "carlos@email.com")
adicionar_contato("João", "11777777777", "joao@email.com")

print("Contatos listados:", listar_contatos())
print("Buscando Ana:", buscar_contato("Ana"))
print("Removendo Carlos:", remover_contato("Carlos"))
print("Contatos listados após remoção:", listar_contatos())
