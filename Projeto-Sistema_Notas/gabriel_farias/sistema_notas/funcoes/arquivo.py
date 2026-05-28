import json
import os


def salvar_nota(turma, aluno, nota1, nota2, nota3):
    """
    Salva os dados de um aluno em um arquivo JSON dentro da pasta /notas.
    """

    # Passo 1: calcular média
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: criar dicionário
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: montar caminho do arquivo
    pasta = "notas"
    os.makedirs(pasta, exist_ok=True)  # garante que a pasta existe
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join(pasta, nome_arquivo)

    # Passo 4: verificar se arquivo existe
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    # Passo 5: adicionar registro
    dados.append(registro)

    # Passo 6: salvar arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma.
    """

    # Passo 1: montar caminho
    pasta = "notas"
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join(pasta, nome_arquivo)

    # Passo 2: verificar existência
    if not os.path.exists(caminho):
        print(f"Nenhum registro encontrado para a turma '{turma}'.")
        return

    # Passo 3: carregar dados
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Passo 4: exibir dados
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(
            f"Nota 1: {registro['nota1']}  |  "
            f"Nota 2: {registro['nota2']}  |  "
            f"Nota 3: {registro['nota3']}"
        )
        print(f"Média : {registro['media']}")
        print("─" * 30)