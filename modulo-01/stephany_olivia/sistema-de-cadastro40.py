# Bibliotecas para trabalhar com arquivos JSON e verificar se o arquivo existe
import json
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "alunos.json"


def carregar():
    # Se o arquivo não existe ainda, retorna uma lista vazia
    if not os.path.exists(ARQUIVO):
        return []
    # Abre o arquivo e lê os dados
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar(alunos):
    # Salva a lista de alunos no arquivo JSON
    with open(ARQUIVO, "w") as f:
        json.dump(alunos, f, indent=4)


def cadastrar_aluno(nome, email, idade, notas):
    alunos = carregar()

    # Gera um ID com base na quantidade de alunos já cadastrados
    novo_id = len(alunos) + 1

    # Cria o dicionário com os dados do novo aluno
    aluno = {
        "id": novo_id,
        "nome": nome,
        "email": email,
        "idade": idade,
        "notas": notas,
        "ativo": True
    }

    # Adiciona o aluno à lista e salva no arquivo
    alunos.append(aluno)
    salvar(alunos)
    print(f"Aluno {nome} cadastrado com sucesso!")
    return aluno


def listar_alunos():
    alunos = carregar()

    # Percorre cada aluno e exibe suas informações com a média calculada
    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Média: {media:.2f}")
    return alunos


def buscar_por_nome(nome):
    alunos = carregar()

    # Percorre a lista e verifica se o nome digitado está no nome do aluno
    for aluno in alunos:
        if nome.lower() in aluno["nome"].lower():
            print(f"Encontrado: {aluno}")
            return aluno

    # Se não encontrar nenhum, avisa o usuário
    print("Aluno não encontrado.")
    return None


def calcular_media_turma():
    alunos = carregar()

    # Junta todas as notas de todos os alunos em uma lista só
    todas_notas = []
    for aluno in alunos:
        todas_notas.extend(aluno["notas"])

    # Calcula e exibe a média geral
    media = sum(todas_notas) / len(todas_notas)
    print(f"Média da turma: {media:.2f}")
    return media


def exportar_relatorio():
    alunos = carregar()

    # Calcula a média individual de cada aluno
    medias = []
    for aluno in alunos:
        media = sum(aluno["notas"]) / len(aluno["notas"])
        medias.append({"nome": aluno["nome"], "media": round(media, 2)})

    # Calcula a média geral, o melhor e o pior aluno
    media_geral = sum(m["media"] for m in medias) / len(medias)
    maior = max(medias, key=lambda x: x["media"])
    menor = min(medias, key=lambda x: x["media"])

    # Monta o dicionário do relatório
    relatorio = {
        "total_alunos": len(alunos),
        "media_geral": round(media_geral, 2),
        "aluno_maior_media": maior,
        "aluno_menor_media": menor
    }

    # Salva o relatório em um arquivo separado
    with open("relatorio_turma.json", "w") as f:
        json.dump(relatorio, f, indent=4)

    print("Relatório exportado!")
    print(relatorio)


# ----- Demonstração -----

cadastrar_aluno("Ana Lima", "ana@email.com", 20, [8.5, 9.0, 7.5])
cadastrar_aluno("Bruno Souza", "bruno@email.com", 22, [6.0, 7.0, 5.5])
cadastrar_aluno("Carla Mendes", "carla@email.com", 19, [10.0, 9.5, 9.8])
cadastrar_aluno("Diego Torres", "diego@email.com", 21, [5.0, 6.5, 4.0])

print("\n--- Lista de alunos ---")
listar_alunos()

print("\n--- Busca por nome ---")
buscar_por_nome("Bruno")

print("\n--- Média da turma ---")
calcular_media_turma()

print("\n--- Relatório ---")
exportar_relatorio()
