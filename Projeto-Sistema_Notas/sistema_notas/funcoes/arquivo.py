# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os


def salvar_nota(turma, aluno, nota1, nota2, nota3):
    """
    Salva os dados de um aluno em um arquivo JSON dentro da pasta /notas.
    """
    # Passo 1: Calcular a média
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Montar o dicionário de registro
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: Montar o caminho do arquivo
    if not os.path.exists("notas"):
        os.makedirs("notas")

    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 4: Verificar se o arquivo já existe
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    # Passo 5: Adicionar o novo registro
    dados.append(registro)

    # Passo 6: Salvar o arquivo atualizado
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.
    """
    # Passo 1: Montar o caminho do arquivo
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 2: Verificar se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"\nNenhum registro encontrado para a turma '{turma}'.")
        return

    # Passo 3: Carregar os dados
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Passo 4: Exibir os registros formatados
    print(f"\n─── Registros da {turma} {'─' * (28 - len(turma))}")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─" * 44)