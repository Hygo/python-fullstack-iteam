"""
Exercício 40 – Desafio Final: Sistema de Cadastro Completo
"""

import json
import uuid
from pathlib import Path

ARQUIVO_ALUNOS = Path("alunos.json")
ARQUIVO_RELATORIO = Path("relatorio_turma.json")


def _carregar_alunos() -> list[dict]:
    """Carrega a lista de alunos do arquivo JSON.

    Returns:
        Lista de dicionários com os dados dos alunos. Retorna lista
        vazia se o arquivo não existir ou estiver corrompido.
    """
    if not ARQUIVO_ALUNOS.exists():
        return []
    try:
        return json.loads(ARQUIVO_ALUNOS.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []


def _salvar_alunos(alunos: list[dict]) -> None:
    """Persiste a lista de alunos no arquivo JSON.

    Args:
        alunos: Lista de dicionários com os dados dos alunos.
    """
    ARQUIVO_ALUNOS.write_text(
        json.dumps(alunos, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def _media_aluno(aluno: dict) -> float:
    """Calcula a média das notas de um aluno.

    Args:
        aluno: Dicionário com os dados do aluno, incluindo 'notas'.

    Returns:
        Média aritmética das notas, ou 0.0 se não houver notas.
    """
    notas = aluno.get("notas", [])
    return round(sum(notas) / len(notas), 2) if notas else 0.0


def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um novo aluno e persiste os dados em alunos.json.

    Args:
        nome: Nome completo do aluno.
        email: Endereço de e-mail do aluno.
        idade: Idade do aluno em anos.
        notas: Lista de notas (floats) obtidas pelo aluno.

    Returns:
        Dicionário com os dados do aluno recém-cadastrado, incluindo
        o campo 'id' gerado automaticamente e 'ativo' definido como True.

    Example:
        >>> aluno = cadastrar_aluno("Ana Lima", "ana@email.com", 20, [8.5, 9.0])
        >>> aluno["nome"]
        'Ana Lima'
    """
    alunos = _carregar_alunos()
    aluno = {
        "id": str(uuid.uuid4())[:8],
        "nome": nome.strip(),
        "email": email.strip().lower(),
        "idade": idade,
        "notas": [round(n, 2) for n in notas],
        "ativo": True,
    }
    alunos.append(aluno)
    _salvar_alunos(alunos)
    return aluno


def listar_alunos() -> list[dict]:
    """Retorna todos os alunos ativos cadastrados.

    Returns:
        Lista de dicionários com os dados de cada aluno ativo.
        Retorna lista vazia se não houver alunos cadastrados.

    Example:
        >>> alunos = listar_alunos()
        >>> isinstance(alunos, list)
        True
    """
    return [a for a in _carregar_alunos() if a.get("ativo", True)]


def buscar_por_nome(nome: str) -> dict | None:
    """Busca um aluno ativo pelo nome (busca parcial, sem distinção de maiúsculas).

    Args:
        nome: Nome ou parte do nome a ser pesquisado.

    Returns:
        Dicionário com os dados do primeiro aluno encontrado,
        ou None se nenhum aluno corresponder à busca.

    Example:
        >>> aluno = buscar_por_nome("ana")
        >>> aluno is None or isinstance(aluno, dict)
        True
    """
    termo = nome.strip().lower()
    for aluno in _carregar_alunos():
        if aluno.get("ativo", True) and termo in aluno["nome"].lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral de todos os alunos ativos.

    Returns:
        Média aritmética das médias individuais de cada aluno ativo,
        arredondada para 2 casas decimais. Retorna 0.0 se não houver
        alunos ou nenhum aluno tiver notas.

    Example:
        >>> media = calcular_media_turma()
        >>> isinstance(media, float)
        True
    """
    ativos = listar_alunos()
    if not ativos:
        return 0.0
    medias = [_media_aluno(a) for a in ativos]
    return round(sum(medias) / len(medias), 2)


def exportar_relatorio() -> None:
    """Gera o arquivo relatorio_turma.json com estatísticas da turma.

    O relatório contém:
        - total_alunos: Quantidade de alunos ativos.
        - media_geral: Média aritmética das notas de toda a turma.
        - aluno_maior_media: Dados do aluno com a maior média.
        - aluno_menor_media: Dados do aluno com a menor média.

    Raises:
        ValueError: Se não houver alunos cadastrados para gerar o relatório.

    Example:
        >>> exportar_relatorio()
        >>> Path("relatorio_turma.json").exists()
        True
    """
    ativos = listar_alunos()
    if not ativos:
        raise ValueError("Nenhum aluno ativo para gerar o relatório.")

    medias = {a["id"]: _media_aluno(a) for a in ativos}
    maior = max(ativos, key=lambda a: medias[a["id"]])
    menor = min(ativos, key=lambda a: medias[a["id"]])

    relatorio = {
        "total_alunos": len(ativos),
        "media_geral": calcular_media_turma(),
        "aluno_maior_media": {**maior, "media": medias[maior["id"]]},
        "aluno_menor_media": {**menor, "media": medias[menor["id"]]},
    }
    ARQUIVO_RELATORIO.write_text(
        json.dumps(relatorio, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Relatório exportado para '{ARQUIVO_RELATORIO}'.")


def _linha(char: str = "─", n: int = 52) -> None:
    print(char * n)


def _exibir_aluno(aluno: dict) -> None:
    media = _media_aluno(aluno)
    print(f"  [{aluno['id']}] {aluno['nome']}")
    print(f"       Email: {aluno['email']}  |  Idade: {aluno['idade']}")
    print(f"       Notas: {aluno['notas']}  →  Média: {media}")


def main() -> None:
    """Executa a demonstração completa do sistema de cadastro."""

    # Garante base limpa a cada execução do script de demonstração
    ARQUIVO_ALUNOS.write_text("[]", encoding="utf-8")

    _linha("═")
    print("   SISTEMA DE CADASTRO DE ALUNOS  –  Exercício 40")
    _linha("═")

    # Cadastrar 4 alunos ─────────────────────────────────────────────────
    print("\n📝 Cadastrando 4 alunos…\n")
    dados = [
        ("Ana Lima",      "ana.lima@escola.com",    20, [8.5, 9.0, 7.5, 10.0]),
        ("Bruno Souza",   "bruno.souza@escola.com", 22, [6.0, 5.5, 7.0, 6.5]),
        ("Carla Mendes",  "carla.m@escola.com",     19, [9.5, 10.0, 9.0, 8.5]),
        ("Diego Torres",  "diego.t@escola.com",     21, [4.5, 5.0, 6.0, 5.5]),
    ]
    for nome, email, idade, notas in dados:
        a = cadastrar_aluno(nome, email, idade, notas)
        print(f"  ✔ {a['nome']} cadastrado  (id: {a['id']})")

    # Listar todos os alunos ─────────────────────────────────────────────
    _linha()
    print("\n📋 Listagem de todos os alunos:\n")
    for aluno in listar_alunos():
        _exibir_aluno(aluno)
        print()

    # Buscar um aluno por nome ───────────────────────────────────────────
    _linha()
    termo = "carla"
    print(f"\n🔍 Buscando por '{termo}':\n")
    encontrado = buscar_por_nome(termo)
    if encontrado:
        _exibir_aluno(encontrado)
    else:
        print("  Nenhum aluno encontrado.")

    # Média geral da turma ───────────────────────────────────────────────
    _linha()
    media = calcular_media_turma()
    print(f"\n📊 Média geral da turma: {media}\n")

    # Exportar relatório ─────────────────────────────────────────────────
    _linha()
    print("\n📁 Exportando relatório…\n")
    exportar_relatorio()

    relatorio = json.loads(ARQUIVO_RELATORIO.read_text(encoding="utf-8"))
    print(f"  Total de alunos : {relatorio['total_alunos']}")
    print(f"  Média geral     : {relatorio['media_geral']}")
    print(f"  Maior média     : {relatorio['aluno_maior_media']['nome']}"
          f"  ({relatorio['aluno_maior_media']['media']})")
    print(f"  Menor média     : {relatorio['aluno_menor_media']['nome']}"
          f"  ({relatorio['aluno_menor_media']['media']})")

    _linha("═")
    print("   Demonstração concluída com sucesso! ✅")
    _linha("═")


if __name__ == "__main__":
    main()