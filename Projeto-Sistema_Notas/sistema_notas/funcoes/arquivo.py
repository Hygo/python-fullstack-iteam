# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os


def salvar_nota(turma, aluno, nota1, nota2, nota3):
    """
    Salva os dados de um aluno em um arquivo JSON dentro da pasta /notas.

    O arquivo será nomeado com o nome da turma (ex: turma_A.json).
    Se o arquivo já existir, o aluno é adicionado à lista existente.
    Se não existir, um novo arquivo é criado.

    Estrutura do JSON salvo:
        [
            {
                "aluno": "Maria Silva",
                "nota1": 8.0,
                "nota2": 7.5,
                "nota3": 9.0,
                "media": 8.17
            },
            ...
        ]

    Parâmetros:
        turma  (str)  : nome da turma (usado como nome do arquivo)
        aluno  (str)  : nome do aluno
        nota1  (float): primeira nota
        nota2  (float): segunda nota
        nota3  (float): terceira nota
    """
    media = round((nota1 + nota2 + nota3) / 3, 2)

    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
    }

    pasta_notas = "notas"
    os.makedirs(pasta_notas, exist_ok=True)
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join(pasta_notas, nome_arquivo)

    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    dados.append(registro)

    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.

    Se o arquivo não existir, exibe uma mensagem informando
    que ainda não há registros para aquela turma.

    Parâmetros:
        turma (str): nome da turma cujos dados serão lidos
    """
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    if not os.path.exists(caminho_arquivo):
        print(f"Nenhum registro encontrado para a turma {turma}.")
        return

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print(f"\n─── Registros da {turma} ───────────────────")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(
            f"Nota 1: {registro['nota1']}  |  "
            f"Nota 2: {registro['nota2']}  |  "
            f"Nota 3: {registro['nota3']}"
        )
        print(f"Média : {registro['media']}")
        print("────────────────────────────────────────────")
