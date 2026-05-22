import json
from typing import List, Dict, Optional

ARQUIVO_AGENDA = "contatos.json"

def _salvar(dados: List[Dict[str, str]]) -> None:
    with open(ARQUIVO_AGENDA, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

def listar_contatos() -> List[Dict[str, str]]:
    try:
        with open(ARQUIVO_AGENDA, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def adicionar_contato(nome: str, telefone: str, email: str) -> None:
    agenda = listar_contatos()
    agenda.append({"nome": nome, "telefone": telefone, "email": email})
    _salvar(agenda)

def buscar_contato(nome: str) -> Optional[Dict[str, str]]:
    agenda = listar_contatos()
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            return contato
    return None

def remover_contato(nome: str) -> bool:
    agenda = listar_contatos()
    com_filtro = [c for c in agenda if c["nome"].lower() != nome.lower()]
    if len(com_filtro) < len(agenda):
        _salvar(com_filtro)
        return True
    return False

adicionar_contato("João Dutra", "9999-8888", "joao@email.com")
adicionar_contato("Maria Clara", "8888-7777", "maria@email.com")
adicionar_contato("Pedro Augusto", "7777-6666", "pedro@email.com")

print("Contatos Carregados:", len(listar_contatos()))
print("Resultado da Busca por 'Maria Clara':", buscar_contato("Maria Clara"))
print("Exclusão de 'João Dutra':", remover_contato("João Dutra"))