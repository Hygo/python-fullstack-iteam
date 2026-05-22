import json
from typing import List, Dict, Any, Optional

ARQUIVO_ALUNOS = "alunos.json"

def _salvar_todos(alunos: List[Dict[str, Any]]) -> None:
    """Função auxiliar para salvar a lista no arquivo."""
    with open(ARQUIVO_ALUNOS, "w", encoding="utf-8") as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)


def listar_alunos() -> List[Dict[str, Any]]:
    """Recupera a listagem completa dos alunos matriculados."""
    try:
        with open(ARQUIVO_ALUNOS, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def cadastrar_aluno(nome: str, email: str, idade: int, notas: List[float]) -> Dict[str, Any]:
    """Cadastra um novo estudante gerando ID autoincremental único."""
    alunos = listar_alunos()
    
    maior_id = 0
    for aluno in alunos:
        if aluno["id"] > maior_id:
            maior_id = aluno["id"]
    novo_id = maior_id + 1
    
    novo_aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True
    }
    
    alunos.append(novo_aluno)
    _salvar_todos(alunos)
    return novo_aluno


def buscar_por_nome(nome: str) -> Optional[Dict[str, Any]]:
    """Procura um estudante baseado em correspondência de nome."""
    alunos = listar_alunos()
    
    for aluno in alunos:
        if nome.lower() in aluno["nome"].lower():
            return aluno
            
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral consolidando todas as notas da turma."""
    alunos = listar_alunos()
    
    soma_total_notas = 0.0
    total_de_notas = 0
    
    for aluno in alunos:
        for nota in aluno["notas"]:
            soma_total_notas += nota
            total_de_notas += 1
            
    if total_de_notas == 0:
        return 0.0
        
    return soma_total_notas / total_de_notas


def exportar_relatorio() -> None:
    """Gera o relatório com total, média geral, maior e menor média."""
    alunos = listar_alunos()
    if not alunos:
        return

    soma_medias = 0.0
    
    aluno_maior_media = ""
    maior_media = -1.0
    
    aluno_menor_media = ""
    menor_media = 11.0

    for aluno in list(alunos):
        soma_notas_aluno = 0.0
        for nota in aluno["notas"]:
            soma_notas_aluno += nota
            
        qtd_notas = len(aluno["notas"])
        media_aluno = soma_notas_aluno / qtd_notas if qtd_notas > 0 else 0.0
        
        soma_medias += media_aluno
        
        if media_aluno > maior_media:
            maior_media = media_aluno
            aluno_maior_media = aluno["nome"]
            
        if media_aluno < menor_media:
            menor_media = media_aluno
            aluno_menor_media = aluno["nome"]

    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": calcular_media_turma(),
        "aluno_maior_media": {
            "aluno": aluno_maior_media,
            "media": round(maior_media, 2)
        },
        "aluno_menor_media": {
            "aluno": aluno_menor_media,
            "media": round(menor_media, 2)
        }
    }

    with open("relatorio_turma.json", "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=4, ensure_ascii=False)


# =DEMONSTRAÇÃO OBRIGATÓRIA=
# Fiz um pouco diferente e cadastrei como "alunos" os 4 melhores jogadores dos LA Lakers

cadastrar_aluno("Kobe Bryant", "blackmamba@lakers.com", 41, [10.0, 9.8, 10.0])
cadastrar_aluno("Magic Johnson", "magic@lakers.com", 64, [9.9, 9.7, 9.8])
cadastrar_aluno("LeBron James", "kingjames@lakers.com", 41, [9.8, 9.9, 9.7])
cadastrar_aluno("Shaquille O'Neal", "shaq@lakers.com", 54, [9.5, 9.2, 9.6])

# Listagem de alunos (jogadores)
print("--- LISTA DE LENDAS DOS LAKERS ---")
todos_alunos = listar_alunos()
for a in todos_alunos:
    print(f"ID: {a['id']} | Jogador: {a['nome']} | Notas de Desempenho: {a['notas']}")

# Buscar um aluno (jogador)
print("\n--- BUSCANDO JOGADOR ---")
resultado_busca = buscar_por_nome("Kobe")
print("Achado:", resultado_busca)

# Exibir média da turma (time)
print("\n--- MÉDIA GERAL DO TIME ---")
print(f"A média de notas do elenco é: {calcular_media_turma():.2f}")

# Exportar relatório
exportar_relatorio()
print("\nRelatório 'relatorio_turma.json' gerado com sucesso!")