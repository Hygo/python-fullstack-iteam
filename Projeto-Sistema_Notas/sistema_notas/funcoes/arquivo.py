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
    """
    # Passo 1: Calcule a média das três notas e arredonde para 2 casas decimais.
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Monte um dicionário chamado `registro`.
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: Monte o caminho do arquivo usando os.path.join().
    # Garante que a pasta "notas" existe antes de salvar o arquivo.
    if not os.path.exists("notas"):
        os.makedirs("notas")
        
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 4: Verifique se o arquivo já existe.
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    # Passo 5: Adicione o `registro` à lista `dados`.
    dados.append(registro)

    # Passo 6: Abra o arquivo para escrita e salve com json.dump().
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.

    Se o arquivo não existir, exibe uma mensagem informando
    que ainda não há registros para aquela turma.
    """
    # Passo 1: Monte o caminho do arquivo da mesma forma que em salvar_nota().
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_arquivo = os.path.join("notas", nome_arquivo)

    # Passo 2: Verifique se o arquivo existe.
    if not os.path.exists(caminho_arquivo):
        print(f"\nAviso: Ainda não há registros para a turma '{turma}'.")
        return

    # Passo 3: Abra o arquivo e carregue os dados com json.load().
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    # Passo 4: Percorra a lista de registros e exiba as informações.
    print(f"\n=== NOTAS DA TURMA: {turma} ===")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─────────────────────────────")