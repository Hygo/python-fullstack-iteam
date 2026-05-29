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

    # TODO (Passo 2): Monte um dicionário chamado `registro` com as chaves:
    #                 "aluno", "nota1", "nota2", "nota3" e "media".

    # TODO (Passo 3): Monte o caminho do arquivo usando os.path.join().
    #                 A pasta deve ser "notas" e o arquivo deve ter o nome
    #                 da turma + ".json" (ex: "notas/turma_A.json").
    #                 Dica: use turma.replace(" ", "_") para evitar espaços.

    # TODO (Passo 4): Verifique se o arquivo já existe com os.path.exists().
    #                 - Se existir: abra com open() e leia a lista atual com json.load().
    #                 - Se não existir: crie uma lista vazia chamada `dados`.

    # TODO (Passo 5): Adicione o `registro` à lista `dados` com .append().

    # TODO (Passo 6): Abra o arquivo para escrita com open() e salve
    #                 com json.dump(). Use indent=4 para formatar.

def salvar_nota(turma, aluno, nota1, nota2, nota3):
    # Passo 1: calcula a média
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: monta o dicionário com os dados do aluno
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: monta o caminho do arquivo
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)
    os.makedirs("notas", exist_ok=True) 

    # Passo 4: se o arquivo já existe, lê a lista atual; senão, começa vazia
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
    else:
        dados = []

    # Passo 5: adiciona o novo registro à lista
    dados.append(registro)

    # Passo 6: grava a lista de volta no arquivo
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.

    Se o arquivo não existir, exibe uma mensagem informando
    que ainda não há registros para aquela turma.

    Parâmetros:
        turma (str): nome da turma cujos dados serão lidos
    """
    # TODO (Passo 1): Monte o caminho do arquivo da mesma forma que em salvar_nota().

    # TODO (Passo 2): Verifique se o arquivo existe.
    #                 Se não existir, imprima uma mensagem adequada e retorne.

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

def ler_notas(turma):
    # Passo 1: monta o caminho (igual ao de salvar_nota)
    nome_arquivo = turma.replace(" ", "_") + ".json"
    caminho = os.path.join("notas", nome_arquivo)

    # Passo 2: se o arquivo não existe, avisa e sai
    if not os.path.exists(caminho):
        print(f"Ainda não há registros para a turma {turma}.")
        return

    # Passo 3: abre e carrega os dados
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    # Passo 4: percorre a lista e exibe cada aluno
    print(f"─── Registros da {turma} ───────────────────")
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─────────────────────────────")