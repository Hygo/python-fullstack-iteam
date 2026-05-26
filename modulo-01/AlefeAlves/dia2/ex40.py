import json
import os
from typing import Optional

ARQUIVO_ALUNOS   = "alunos.json"
ARQUIVO_RELATORIO = "relatorio_turma.json"


def _ler_alunos() -> list[dict]:
    if not os.path.exists(ARQUIVO_ALUNOS):
        return []
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        return json.load(f)


def _salvar_alunos(alunos: list[dict]) -> None:
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=2, ensure_ascii=False)


def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um novo aluno e persiste no arquivo JSON.

    Args:
        nome: Nome completo do aluno.
        email: E-mail do aluno.
        idade: Idade em anos.
        notas: Lista de notas (valores de 0.0 a 10.0).

    Returns:
        Dicionário com os dados do aluno recém-cadastrado.
    """
    alunos = _ler_alunos()
    novo_id = (max(a["id"] for a in alunos) + 1) if alunos else 1
    aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True,
    }
    alunos.append(aluno)
    _salvar_alunos(alunos)
    return aluno


def listar_alunos() -> list[dict]:
    """Retorna todos os alunos cadastrados.

    Returns:
        Lista de dicionários com os dados de cada aluno.
    """
    return _ler_alunos()


def buscar_por_nome(nome: str) -> Optional[dict]:
    """Busca um aluno pelo nome (busca parcial, sem distinção de maiúsculas).

    Args:
        nome: Nome ou parte do nome a pesquisar.

    Returns:
        Dicionário do primeiro aluno encontrado ou None.
    """
    for aluno in _ler_alunos():
        if nome.lower() in aluno["nome"].lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral de notas de todos os alunos ativos.

    Returns:
        Média aritmética das médias individuais dos alunos. Retorna 0.0 se não houver alunos.
    """
    alunos = _ler_alunos()
    if not alunos:
        return 0.0
    medias = [sum(a["notas"]) / len(a["notas"]) for a in alunos if a["notas"]]
    return sum(medias) / len(medias) if medias else 0.0


def exportar_relatorio() -> None:
    """Gera relatorio_turma.json com estatísticas da turma.

    O relatório inclui: total de alunos, média geral, aluno com maior média
    e aluno com menor média.
    """
    alunos = _ler_alunos()
    if not alunos:
        print("Nenhum aluno cadastrado para gerar relatório.")
        return

    def media(aluno: dict) -> float:
        return sum(aluno["notas"]) / len(aluno["notas"]) if aluno["notas"] else 0.0

    melhor = max(alunos, key=media)
    pior   = min(alunos, key=media)

    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": round(calcular_media_turma(), 2),
        "aluno_maior_media": {"nome": melhor["nome"], "media": round(media(melhor), 2)},
        "aluno_menor_media": {"nome": pior["nome"],   "media": round(media(pior), 2)},
    }

    with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)

    print(f"Relatório exportado para '{ARQUIVO_RELATORIO}'.")


# ── Demonstração obrigatória ──────────────────────────────────────────────────

if os.path.exists(ARQUIVO_ALUNOS):
    os.remove(ARQUIVO_ALUNOS)

cadastrar_aluno("Álefe Alves",  "alefe@aluno.com",   21, [9.5, 8.0, 10.0])
cadastrar_aluno("Amanda de Brito", "amanda@aluno.com", 27, [7.5, 8.5,  9.0])
cadastrar_aluno("Luciano dos Santos",   "luciano@aluno.com",    23, [6.0, 7.0,  6.5])
cadastrar_aluno("Kaio Souza",       "kaio@aluno.com",      23, [10.0, 9.5, 9.0])

print("===== LISTA DE ALUNOS =====")
for a in listar_alunos():
    media = sum(a["notas"]) / len(a["notas"])
    print(f"  [{a['id']}] {a['nome']:<20} notas={a['notas']}  média={media:.1f}")

print("\n--- Busca por 'Lucas' ---")
encontrado = buscar_por_nome("Lucas")
print(f"  {encontrado}")

print(f"\n--- Média geral da turma ---")
print(f"  {calcular_media_turma():.2f}")

print()
exportar_relatorio()

with open(ARQUIVO_RELATORIO, "r", encoding="utf-8") as f:
    print(json.dumps(json.load(f), indent=2, ensure_ascii=False))