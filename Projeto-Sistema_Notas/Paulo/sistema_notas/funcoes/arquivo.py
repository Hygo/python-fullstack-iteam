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
    # Passo 1: Calcula a média
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Cria o dicionário
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Garante a existência da pasta
    if not os.path.exists("notas"):
        os.makedirs("notas")

    # Passo 3: Caminho do arquivo
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 4: Verifica o arquivo e carrega os dados
    dados = []
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []

    # Passo 5: Adiciona o novo registro
    dados.append(registro)

    # Passo 6: Salva no arquivo
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.

    Se o arquivo não existir, exibe uma mensagem informando
    que ainda não há registros para aquela turma.

    Parâmetros:
        turma (str): nome da turma cujos dados serão lidos
    """
    # Passo 1: Caminho do arquivo
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 2: Verifica existência
    if not os.path.exists(caminho_arquivo):
        print(f"Ainda não há registros para a turma '{turma}'.")
        return

    # Passo 3: Carrega os dados
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except Exception:
        print("Erro ao ler o arquivo de notas.")
        return

    # Passo 4: Exibe os registros
    print(f"\n─── Registros da Turma {turma} ───────────────────")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("────────────────────────────────────────────")
