import json
from typing import List, Dict, Optional

ARQUIVO = "alunos.json"


def carregar_alunos() -> List[Dict]:
    """
    Carrega os alunos do arquivo JSON.

    Returns:
        List[Dict]: Lista de alunos cadastrados.
    """
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def salvar_alunos(alunos: List[Dict]) -> None:
    """
    Salva a lista de alunos no arquivo JSON.

    Args:
        alunos (List[Dict]): Lista de alunos.
    """
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=2, ensure_ascii=False)


def cadastrar_aluno(nome: str, email: str, idade: int, notas: List[float]) -> Dict:
    """
    Cadastra um novo aluno.

    Args:
        nome (str): Nome do aluno.
        email (str): Email do aluno.
        idade (int): Idade do aluno.
        notas (List[float]): Lista de notas do aluno.

    Returns:
        Dict: Dicionário com os dados do aluno cadastrado.
    """
    alunos = carregar_alunos()
    novo_id = len(alunos) + 1
    aluno = {
        "id": novo_id,
        "nome": nome.strip().title(),
        "email": email.lower(),
        "idade": idade,
        "notas": notas,
        "ativo": True
    }
    alunos.append(aluno)
    salvar_alunos(alunos)
    return aluno


def listar_alunos() -> List[Dict]:
    """
    Lista todos os alunos cadastrados.

    Returns:
        List[Dict]: Lista de alunos.
    """
    return carregar_alunos()


def buscar_por_nome(nome: str) -> Optional[Dict]:
    """
    Busca um aluno pelo nome.

    Args:
        nome (str): Nome do aluno.

    Returns:
        Optional[Dict]: Aluno encontrado ou None.
    """
    alunos = carregar_alunos()
    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """
    Calcula a média geral da turma.

    Returns:
        float: Média geral das notas de todos os alunos.
    """
    alunos = carregar_alunos()
    todas_notas = [nota for aluno in alunos for nota in aluno["notas"]]
    return sum(todas_notas) / len(todas_notas) if todas_notas else 0.0


def exportar_relatorio() -> None:
    """
    Exporta um relatório da turma para relatorio_turma.json.

    Relatório contém:
    - Total de alunos
    - Média geral da turma
    - Aluno com maior média
    - Aluno com menor média
    """
    alunos = carregar_alunos()
    if not alunos:
        return

    medias = [(aluno["nome"], sum(aluno["notas"]) / len(aluno["notas"])) for aluno in alunos]
    maior = max(medias, key=lambda x: x[1])
    menor = min(medias, key=lambda x: x[1])

    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": calcular_media_turma(),
        "maior_media": {"nome": maior[0], "media": maior[1]},
        "menor_media": {"nome": menor[0], "media": menor[1]}
    }

    with open("relatorio_turma.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False)


# --- Demonstração ---
print("--- Sistema de Cadastro de Alunos ---")

# 1. Cadastrar 4 alunos
cadastrar_aluno("Alice", "alice@email.com", 20, [8.5, 9.0, 7.5])
cadastrar_aluno("Bruno", "bruno@email.com", 22, [6.0, 7.0, 6.5])
cadastrar_aluno("Carla", "carla@email.com", 19, [9.5, 9.0, 10.0])
cadastrar_aluno("Daniel", "daniel@email.com", 21, [5.0, 6.0, 5.5])

# 2. Listar alunos
print("\nLista de alunos:")
for aluno in listar_alunos():
    print(f"{aluno['id']} - {aluno['nome']} ({aluno['email']}) - Idade: {aluno['idade']} - Ativo: {aluno['ativo']}")

# 3. Buscar um aluno
print("\nBuscando aluno 'Carla':")
print(buscar_por_nome("Carla"))

# 4. Exibir média da turma
print("\nMédia geral da turma:", calcular_media_turma())

# 5. Exportar relatório
exportar_relatorio()
print("\nRelatório exportado para relatorio_turma.json")
