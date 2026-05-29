<<<<<<< HEAD
# ============================================================
# MÓDULO: arquivo.py
# Responsável por salvar e ler notas no formato JSON
# ============================================================

import json
import os

# Pasta raiz do projeto (sistema_notas/), independente de onde o script é executado
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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
    def calcular_media(n1, n2, n3):
        media = (n1 + n2 + n3) / 3
        return round(media, 2)

    def criar_registro(aluno, nota1, nota2, nota3):
        registro = {
            "aluno": aluno,
            "nota1": nota1,
            "nota2": nota2,
            "nota3": nota3,
            "media": calcular_media(nota1, nota2, nota3)
        }
        return registro

    def montar_caminho(turma):
        nome_arquivo = turma.replace(" ", "_") + ".json"
        caminho_gerado = os.path.join(BASE_DIR, "notas", nome_arquivo)
        return caminho_gerado

    def salvar_dados(caminho_do_arquivo, registro_do_aluno):
        # Garante que a pasta 'notas' exista para não dar erro ao salvar o arquivo
        pasta_notas = os.path.join(BASE_DIR, "notas")
        if not os.path.exists(pasta_notas):
            os.makedirs(pasta_notas)

        if os.path.exists(caminho_do_arquivo):
            with open(caminho_do_arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
        else:
            dados = []

        dados.append(registro_do_aluno)

        with open(caminho_do_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    # Chama as funções internas na ordem correta
    registro = criar_registro(aluno, nota1, nota2, nota3)
    caminho = montar_caminho(turma)
    salvar_dados(caminho, registro)


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

    def montar_caminho(turma):
        nome_arquivo = turma.replace(" ", "_") + ".json"
        caminho = os.path.join(BASE_DIR, "notas", nome_arquivo)
        return caminho

    def verificar_arquivo(caminho):
        if not os.path.exists(caminho):
            print(f"Ainda não há registros para a turma '{turma}'.")
            return False
        return True

    def ler_dados(caminho):
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    # Chama as funções internas na ordem correta
    caminho = montar_caminho(turma)
    if not verificar_arquivo(caminho):
        return
    dados = ler_dados(caminho)
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']}  |  Nota 2: {registro['nota2']}  |  Nota 3: {registro['nota3']}")
        print(f"Média : {registro['media']}")
        print("─" * 30)
=======
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

    pass  # ← apague esta linha e escreva seu código aqui


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

    pass  # ← apague esta linha e escreva seu código aqui
>>>>>>> ef17bb8c49c7d5951871fb6a5460e3d9b160d3ae
