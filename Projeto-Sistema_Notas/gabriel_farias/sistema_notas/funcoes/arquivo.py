# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os

# Diretório base: sempre a pasta onde este arquivo (arquivo.py) está
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_NOTAS = os.path.join(BASE_DIR, "notas")


def salvar_nota(turma, aluno, nota1, nota2, nota3):
    media = round((nota1 + nota2 + nota3) / 3, 2)

    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join(PASTA_NOTAS, nome_arquivo)

    os.makedirs(PASTA_NOTAS, exist_ok=True)

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    dados.append(registro)

    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def ler_notas(turma):
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join(PASTA_NOTAS, nome_arquivo)

    if not os.path.exists(caminho):
        print(f"Nenhum registro encontrado para a turma '{turma}'.")
        return

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    print(f"\n{'='*35}")
    print(f"  Turma: {turma}")
    print(f"{'='*35}")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─" * 35)