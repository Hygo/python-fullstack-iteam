# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os


def salvar_nota(turma, aluno, nota1, nota2, nota3):
    # Passo 1: Calcula a média arredondada
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Monta o dicionário com os dados do aluno
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: Monta o caminho do arquivo
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)

    # Passo 4: Lê os dados existentes ou cria lista vazia
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        os.makedirs("notas", exist_ok=True)
        dados = []

    # Passo 5: Adiciona o novo registro
    dados.append(registro)

    # Passo 6: Salva a lista atualizada no arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def ler_notas(turma):
    # Passo 1: Monta o caminho do arquivo
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)

    # Passo 2: Verifica se o arquivo existe
    if not os.path.exists(caminho):
        print(f"Nenhum registro encontrado para a turma '{turma}'.")
        return

    # Passo 3: Carrega os dados do arquivo
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Passo 4: Exibe os dados formatados
    print(f"\n{'='*35}")
    print(f"  Turma: {turma}")
    print(f"{'='*35}")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─" * 35)