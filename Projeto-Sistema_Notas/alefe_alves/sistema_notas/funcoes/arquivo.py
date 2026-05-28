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
    # TODO (Passo 1): Calcule a média das três notas.
    #                 Arredonde para 2 casas decimais com round().
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # TODO (Passo 2): Monte um dicionário chamado `registro` com as chaves:
    #                 "aluno", "nota1", "nota2", "nota3" e "media".
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # TODO (Passo 3): Monte o caminho do arquivo usando os.path.join().
    #                 A pasta deve ser "notas" e o arquivo deve ter o nome
    #                 da turma + ".json" (ex: "notas/turma_A.json").
    #                 Dica: use turma.replace(" ", "_") para evitar espaços.
    nome_turma = turma.replace(" ", "_")
    caminho = os.path.join("notas", nome_turma + ".json")

    # TODO (Passo 4): Verifique se o arquivo já existe com os.path.exists().
    #                 - Se existir: abra com open() e leia a lista atual com json.load().
    #                 - Se não existir: crie uma lista vazia chamada `dados`.
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    else:
        dados = []

    # TODO (Passo 5): Adicione o `registro` à lista `dados` com .append().
    dados.append(registro)

    # TODO (Passo 6): Abra o arquivo para escrita com open() e salve
    #                 com json.dump(). Use indent=4 para formatar.
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.

    Se o arquivo não existir, exibe uma mensagem informando
    que ainda não há registros para aquela turma.

    Parâmetros:
        turma (str): nome da turma cujos dados serão lidos
    """
    # TODO (Passo 1): Monte o caminho do arquivo da mesma forma que em salvar_nota().
    nome_turma = turma.replace(" ", "_")
    caminho = os.path.join("notas", nome_turma + ".json")

    # TODO (Passo 2): Verifique se o arquivo existe.
    #                 Se não existir, imprima uma mensagem adequada e retorne.
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
    else:
        print("Não existe registro da turma informada.")
        return

    # TODO (Passo 3): Abra o arquivo com open() e carregue os dados com json.load().

    # TODO (Passo 4): Percorra a lista de registros com um loop for.
    #                 Para cada registro, exiba: nome do aluno, as 3 notas e a média.
    #                 Formate a saída de forma legível para o usuário.
    #                 Exemplo de exibição:
    #
    #                 Aluno : Maria Silva
    #                 Nota 1: 8.0  |  Nota 2: 7.5  |  Nota 3: 9.0
    #                 Média : 8.17
    #                 ─────────────────────────────
    for aluno in dados:
        print(f"""
        Aluno : {aluno["aluno"]}
        Nota 1: {aluno["nota1"]}  |  Nota 2: {aluno["nota2"]}  |  Nota 3: {aluno["nota3"]}
        Média : {aluno["media"]}
        ─────────────────────────────""")
