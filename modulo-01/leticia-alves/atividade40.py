 # Exercício 40 – Desafio Final: Sistema de Cadastro Completo
 #Aluna: Leticia Alves

import json

ARQUIVO = "alunos.json"


def carregar() -> list[dict]:
    """Carrega os alunos do arquivo JSON.

    Returns:
        list[dict]: Uma lista contendo os dicionários dos alunos.
            Retorna uma lista vazia se o arquivo não existir.
    """
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []


def salvar(alunos: list[dict]) -> None:
    """Salva a lista de alunos no arquivo JSON.

    Args:
        alunos (list[dict]): A lista de dicionários dos alunos a ser salva.
    """
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)


def cadastrar_aluno(
    nome: str, email: str, idade: int, notas: list[float]
) -> dict:
    """Cadastra um novo aluno no sistema e persiste no arquivo JSON.

    Args:
        nome (str): Nome completo do aluno.
        email (str): Endereço de e-mail do aluno.
        idade (int): Idade do aluno.
        notas (list[float]): Lista com as notas do aluno.

    Returns:
        dict: O dicionário do aluno recém-criado com ID e status ativo.
    """
    alunos = carregar()

    aluno = {
        "id": len(alunos) + 1,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True,
    }

    alunos.append(aluno)
    salvar(alunos)
    return aluno


def listar_alunos() -> list[dict]:
    """Lista todos os alunos cadastrados no sistema.

    Returns:
        list[dict]: Lista com todos os dicionários de alunos.
    """
    return carregar()


def buscar_por_nome(nome: str) -> dict | None:
    """Busca um aluno no sistema pelo nome.

    A busca ignora diferenças entre letras maiúsculas e minúsculas.

    Args:
        nome (str): O nome do aluno a ser buscado.

    Returns:
        dict | None: O dicionário do aluno se encontrado, ou None caso contrário.
    """
    for aluno in carregar():
        if aluno["nome"].lower() == nome.lower():
            return aluno
    return None


def calcular_media_turma() -> float:
    """Calcula a média geral de todas as notas de todos os alunos da turma.

    Returns:
        float: A média geral da turma. Retorna 0.0 se não houver notas.
    """
    alunos = carregar()
    if not alunos:
        return 0.0

    total_notas = 0
    qtd_notas = 0

    for aluno in alunos:
        total_notas += sum(aluno["notas"])
        qtd_notas += len(aluno["notas"])

    return total_notas / qtd_notas


def exportar_relatorio() -> None:
    """Gera um relatório estatístico da turma e salva em 'relatorio_turma.json'.

    O relatório contém o total de alunos, a média geral da turma, e os dados
    completos dos alunos com a maior e a menor média observadas.
    """
    alunos = carregar()
    if not alunos:
        return

    aluno_maior = alunos[0]
    aluno_menor = alunos[0]

    for aluno in alunos:
        media_atual = sum(aluno["notas"]) / len(aluno["notas"])
        media_maior = sum(aluno_maior["notas"]) / len(aluno_maior["notas"])
        media_menor = sum(aluno_menor["notas"]) / len(aluno_menor["notas"])

        if media_atual > media_maior:
            aluno_maior = aluno
        if media_atual < media_menor:
            aluno_menor = aluno

    # Ajustado para passar o "aluno" (objeto/dict completo) conforme pede o enunciado
    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": calcular_media_turma(),
        "aluno_maior_media": aluno_maior,
        "aluno_menor_media": aluno_menor,
    }

    with open("relatorio_turma.json", "w") as f:
        json.dump(relatorio, f, indent=4)


# =====================================================================
# DEMONSTRAÇÃO OBRIGATÓRIA
# =====================================================================
if __name__ == "__main__":
    print("--- INICIANDO SISTEMA DE CADASTRO ---")

    # Limpa o arquivo para o teste rodar limpo
    open(ARQUIVO, "w").close()

    # 1. Cadastrar 4 alunos
    print("\n[Passo 1] Cadastrando 4 alunos...")
    cadastrar_aluno("Leticia", "leticia@email.com", 20, [8.0, 9.0])
    cadastrar_aluno("Rafael", "rafael@email.com", 21, [7.0, 6.0])
    cadastrar_aluno("Maria", "maria@email.com", 19, [10.0, 9.5])
    cadastrar_aluno("Lucas", "lucas@email.com", 22, [5.0, 6.5])
    print("Alunos cadastrados com sucesso!")

    # 2. Listar alunos
    print("\n[Passo 2] Listando alunos salvos:")
    todos_alunos = listar_alunos()
    for aluno in todos_alunos:
        print(f"- ID: {aluno['id']} | Nome: {aluno['nome']}")

    # 3. Buscar um aluno por nome
    print("\n[Passo 3] Buscando pela 'Maria':")
    aluno_encontrado = buscar_por_nome("Maria")
    print(aluno_encontrado)

    # 4. Exibir média da turma
    print("\n[Passo 4] Calculando média geral da turma...")
    media = calcular_media_turma()
    print(f"Média da turma: {media:.2f}")

    # 5. Exportar relatório
    print("\n[Passo 5] Exportando relatório...")
    exportar_relatorio()
    print("Arquivo 'relatorio_turma.json' gerado com sucesso!")