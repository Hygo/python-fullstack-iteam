import json
import os

ARQUIVO_ALUNOS = "alunos.json"

def _carregar_bd() -> list[dict]:
    if not os.path.exists(ARQUIVO_ALUNOS):
        return []
    with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
        return json.load(f)

def _salvar_bd(dados: list[dict]) -> None:
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """
    Cadastra um novo aluno no sistema.

    Args:
        nome (str): O nome do aluno.
        email (str): O e-mail do aluno.
        idade (int): A idade do aluno.
        notas (list[float]): A lista de notas do aluno.

    Returns:
        dict: O dicionário do aluno recém-criado.
    """
    alunos = _carregar_bd()
    novo_id = max([a.get("id", 0) for a in alunos], default=0) + 1
    novo_aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True
    }
    alunos.append(novo_aluno)
    _salvar_bd(alunos)
    return novo_aluno

def listar_alunos() -> list[dict]:
    """
    Lista todos os alunos cadastrados.

    Returns:
        list[dict]: A lista de todos os alunos.
    """
    return _carregar_bd()

def buscar_por_nome(nome: str) -> dict | None:
    """
    Busca um aluno pelo nome.

    Args:
        nome (str): O nome a ser buscado.

    Returns:
        dict | None: Os dados do aluno ou None se não encontrado.
    """
    for aluno in _carregar_bd():
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None

def calcular_media_turma() -> float:
    """
    Calcula a média geral de todas as notas da turma.

    Returns:
        float: A média da turma ou 0.0 se não houver notas.
    """
    alunos = _carregar_bd()
    todas_notas = []
    for a in alunos:
        todas_notas.extend(a["notas"])
    
    if not todas_notas:
        return 0.0
    return sum(todas_notas) / len(todas_notas)

def exportar_relatorio() -> None:
    """
    Exporta um relatório da turma em formato JSON.
    Inclui o total de alunos, média geral e os alunos com maior e menor média.
    """
    alunos = _carregar_bd()
    if not alunos:
        print("Nenhum aluno para gerar relatório.")
        return
        
    def media(aluno):
        return sum(aluno["notas"]) / len(aluno["notas"]) if aluno["notas"] else 0.0
        
    media_geral = calcular_media_turma()
    aluno_maior = max(alunos, key=media)
    aluno_menor = min(alunos, key=media)
    
    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": round(media_geral, 2),
        "maior_media": {"nome": aluno_maior["nome"], "media": round(media(aluno_maior), 2)},
        "menor_media": {"nome": aluno_menor["nome"], "media": round(media(aluno_menor), 2)}
    }
    
    with open("relatorio_turma.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)

# Demonstração
if os.path.exists(ARQUIVO_ALUNOS):
    os.remove(ARQUIVO_ALUNOS)

cadastrar_aluno("Alice", "alice@email.com", 20, [8.0, 9.0, 10.0])
cadastrar_aluno("Bruno", "bruno@email.com", 22, [5.0, 6.0, 5.5])
cadastrar_aluno("Carla", "carla@email.com", 19, [9.5, 9.5, 9.0])
cadastrar_aluno("Diego", "diego@email.com", 21, [7.0, 7.5, 8.0])

print("Total alunos listados:", len(listar_alunos()))
print("Buscando Carla:", buscar_por_nome("Carla")["nome"])
print(f"Média da Turma: {calcular_media_turma():.2f}")
exportar_relatorio()
print("Relatório exportado para relatorio_turma.json")
