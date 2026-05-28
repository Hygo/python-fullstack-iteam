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
    # Passo 1: Calcule a média das três notas.
    #          Arredonde para 2 casas decimais com round().
    media = round((nota1 + nota2 + nota3) / 3, 2)

    # Passo 2: Monte um dicionário chamado `registro` com as chaves:
    #          "aluno", "nota1", "nota2", "nota3" e "media".
    registro = {
        "aluno": aluno,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media
    }

    # Passo 3: Monte o caminho do arquivo usando os.path.join().
    #          A pasta deve ser "notas" e o arquivo deve ter o nome
    #          da turma + ".json" (ex: "notas/turma_A.json").
    #          Dica: use turma.replace(" ", "_") para evitar espaços.
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_pasta = "notas"
    
    # Garante que a pasta 'notas' existe antes de salvar
    if not os.path.exists(caminho_pasta):
        os.makedirs(caminho_pasta)
        
    caminho_completo = os.path.join(caminho_pasta, nome_arquivo)

    # Passo 4: Verifique se o arquivo já existe com os.path.exists().
    #          - Se existir: abra com open() e leia a lista atual com json.load().
    #          - Se não existir: crie uma lista vazia chamada `dados`.
    if os.path.exists(caminho_completo):
        try:
            with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
        except json.JSONDecodeError:
            dados = []
    else:
        dados = []

    # Passo 5: Adicione o `registro` à lista `dados` com .append().
    dados.append(registro)

    # Passo 6: Abra o arquivo para escrita com open() e salve
    #          com json.dump(). Use indent=4 para formatar.
    with open(caminho_completo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def ler_notas(turma):
    """
    Lê e exibe todas as notas de uma turma salvas no arquivo JSON.
    """
    # Passo 1: Monte o caminho do arquivo da mesma forma que em salvar_nota().
    nome_arquivo = f"{turma.replace(' ', '_')}.json"
    caminho_completo = os.path.join("notas", nome_arquivo)

    # Passo 2: Verifique se o arquivo existe.
    #          Se não existir, imprima uma mensagem adequada e retorne.
    if not os.path.exists(caminho_completo):
        topo = f"─── Registros da {turma} "
        print(f"\n{topo.ljust(44, '─')}")
        print("Nenhum aluno cadastrado ainda.")
        print("─" * 44 + "\n")
        return

    # Passo 3: Abra o arquivo com open() e carregue os dados com json.load().
    with open(caminho_completo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    # Passo 4: Percorra a lista de registros com um loop for.
    #          Para cada registro, exiba os dados formatados exatamente como no modelo.
    topo = f"─── Registros da {turma} "
    print(f"\n{topo.ljust(44, '─')}")
    
    for registro in dados:
        print(f"Aluno : {registro['aluno']}")
        print(f"Nota 1: {registro['nota1']:.1f}  |  Nota 2: {registro['nota2']:.1f}  |  Nota 3: {registro['nota3']:.1f}")
        print(f"Média : {registro['media']:.2f}")
        
    print("─" * 44 + "\n")