import json
import os

DIRETORIO_DO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

# Nome dos arquivos de persistência e relatório
ARQUIVO_BANCO = os.path.join(DIRETORIO_DO_SCRIPT,"alunos.json")
ARQUIVO_RELATORIO = os.path.join(DIRETORIO_DO_SCRIPT,"relatorio_turma.json")


def _carregar_dados() -> list[dict]:
    """Carrega os dados do arquivo JSON de persistência.

    Returns:
        list[dict]: Lista contendo os dicionários de alunos cadastrados.
    """
    if not os.path.exists(ARQUIVO_BANCO):
        return []
    try:
        with open(ARQUIVO_BANCO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (json.JSONDecodeError, IOError):
        return []


def _salvar_dados(dados: list[dict]) -> None:
    """Salva a lista de alunos atualizada no arquivo JSON de persistência.

    Args:
        dados (list[dict]): Lista com todos os alunos do sistema.
    """
    try:
        with open(ARQUIVO_BANCO, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except IOError as erro:
        print(f"Erro ao persistir dados no arquivo: {erro}")


def cadastrar_aluno(nome: str, email: str, idade: int, notas: list[float]) -> dict:
    """Cadastra um novo aluno no sistema com um ID incremental exclusivo.

    Args:
        nome (str): Nome completo do aluno.
        email (str): Endereço de e-mail do aluno.
        idade (int): Idade do aluno.
        notas (list[float]): Lista contendo as notas do aluno.

    Returns:
        dict: O dicionário do aluno recém-criado e salvo.
    """
    alunos = _carregar_dados()
    
    # Gera ID incremental baseado no maior ID existente
    novo_id = max([aluno["id"] for aluno in alunos], default=0) + 1
    
    novo_aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True
    }
    
    alunos.append(novo_aluno)
    _salvar_dados(alunos)
    return novo_aluno


def listar_alunos() -> list[dict]:
    """Retorna a lista completa de todos os alunos cadastrados.

    Returns:
        list[dict]: Lista de dicionários contendo os dados dos alunos.
    """
    return _carregar_dados()


def buscar_por_nome(nome: str) -> dict | None:
    """Busca o primeiro aluno que possua o nome correspondente (case-insensitive).

    Args:
        nome (str): Nome ou parte do nome do aluno a ser buscado.

    Returns:
        dict | None: Dicionário do aluno encontrado ou None se não existir.
    """
    alunos = _carregar_dados()
    nome_busca = nome.strip().lower()
    
    for aluno in alunos:
        if nome_busca in aluno["nome"].lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral baseada em todas as notas de todos os alunos.

    Returns:
        float: Valor da média aritmética da turma. Retorna 0.0 se não houver notas.
    """
    alunos = _carregar_dados()
    todas_as_notas = []
    
    for aluno in list(alunos):
        todas_as_notas.extend(aluno["notas"])
        
    if not todas_as_notas:
        return 0.0
        
    return sum(todas_as_notas) / len(todas_as_notas)


def exportar_relatorio() -> None:
    """Gera o arquivo 'relatorio_turma.json' contendo estatísticas detalhadas.

    Estatísticas calculadas: total de alunos, média geral da turma,
    dados do aluno com a maior média e dados do aluno com a menor média.
    """
    alunos = _carregar_dados()
    
    if not alunos:
        print("⚠️ Não há alunos cadastrados para exportar o relatório.")
        return

    # Helper inline para calcular a média individual de um aluno
    def obter_media_aluno(a: dict) -> float:
        return sum(a["notas"]) / len(a["notas"]) if a["notas"] else 0.0

    aluno_maior = max(alunos, key=obter_media_aluno)
    aluno_menor = min(alunos, key=obter_media_aluno)

    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": round(calcular_media_turma(), 2),
        "aluno_maior_media": {
            "nome": aluno_maior["nome"],
            "media": round(obter_media_aluno(aluno_maior), 2)
        },
        "aluno_menor_media": {
            "nome": aluno_menor["nome"],
            "media": round(obter_media_aluno(aluno_menor), 2)
        }
    }

    try:
        with open(ARQUIVO_RELATORIO, "w", encoding="utf-8") as arquivo:
            json.dump(relatorio, arquivo, indent=4, ensure_ascii=False)
        print(f"✅ Relatório da turma exportado com sucesso para '{ARQUIVO_RELATORIO}'!")
    except IOError as erro:
        print(f"❌ Erro ao exportar o arquivo de relatório: {erro}")


# ==============================================================================
# DEMONSTRAÇÃO OBRIGATÓRIA DOS REQUISITOS
# ==============================================================================
if __name__ == "__main__":
    # Limpando simulações anteriores para garantir uma execução limpa
    if os.path.exists(ARQUIVO_BANCO):
        os.remove(ARQUIVO_BANCO)

    print("--- 1. Cadastrando 4 alunos ---")
    cadastrar_aluno("Rafael Nóbrega", "rafael@email.com", 24, [9.0, 8.5, 10.0])
    cadastrar_aluno("Maria Eduarda", "duda@email.com", 24, [7.0, 8.5, 7.0])
    cadastrar_aluno("Leticia Alves", "leticia@email.com", 20, [7.5, 8.0, 8.5])
    cadastrar_aluno("Diego Mendes", "diego@email.com", 21, [4.0, 5.0, 3.5])
    print("Alunos cadastrados com sucesso!\n")

    print("--- 2. Listando alunos ---")
    lista = listar_alunos()
    for aluno in lista:
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']:<12} | Notas: {aluno['notas']}")
    print()

    print("--- 3. Buscando um aluno ---")
    aluno_buscado = buscar_por_nome("Carla")
    if aluno_buscado:
        print(f"Encontrado! -> Email: {aluno_buscado['email']} | Idade: {aluno_buscado['idade']}")
    else:
        print("Aluno não encontrado.")
    print()

    print("--- 4. Exibindo média geral ---")
    media_geral = calcular_media_turma()
    print(f"Média geral de todas as notas da turma: {media_geral:.2f}\n")

    print("--- 5. Exportando relatório ---")
    exportar_relatorio()
