import json
from typing import List, Dict

def carregar_dados(caminho: str) -> List[Dict]:
    """
    Carrega os dados de clientes de um arquivo JSON.

    Args:
        caminho (str): Caminho do arquivo JSON.

    Returns:
        List[Dict]: Lista de dicionários com os dados dos clientes.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def normalizar_dados(dados: List[Dict]) -> List[Dict]:
    """
    Normaliza os dados dos clientes:
    - Nome capitalizado
    - Email em minúsculas
    - Telefone formatado (DDD + número)

    Args:
        dados (List[Dict]): Lista de clientes.

    Returns:
        List[Dict]: Lista de clientes normalizados.
    """
    normalizados = []
    for cliente in dados:
        nome = cliente["nome"].strip().title()
        email = cliente["email"].strip().lower()
        telefone = cliente["telefone"].replace(" ", "").replace("-", "")
        if len(telefone) == 11:
            telefone = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
        normalizados.append({"nome": nome, "email": email, "telefone": telefone})
    return normalizados


def enriquecer_dados(dados: List[Dict]) -> List[Dict]:
    """
    Enriquece os dados adicionando um campo 'status'
    baseado no domínio do email.

    Args:
        dados (List[Dict]): Lista de clientes normalizados.

    Returns:
        List[Dict]: Lista de clientes enriquecidos.
    """
    enriquecidos = []
    for cliente in dados:
        dominio = cliente["email"].split("@")[-1]
        status = "Interno" if dominio.endswith("empresa.com") else "Externo"
        cliente["status"] = status
        enriquecidos.append(cliente)
    return enriquecidos


def exportar_resultado(dados: List[Dict], caminho: str) -> None:
    """
    Exporta os dados tratados para um arquivo JSON.

    Args:
        dados (List[Dict]): Lista de clientes tratados.
        caminho (str): Caminho do arquivo de saída.
    """
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


# --- Demonstração do Pipeline ---

# Criando um JSON inicial com dados irregulares
clientes_irregulares = [
    {"nome": "  fernanda costa ", "email": "FERNANDA@EMPRESA.COM", "telefone": "55999999999"},
    {"nome": "bruno   ", "email": "Bruno@GMAIL.com", "telefone": "55888888888"},
    {"nome": "carla", "email": "Carla@empresa.com", "telefone": "55777777777"},
    {"nome": "joão   silva", "email": "Joao@Yahoo.Com", "telefone": "55666666666"},
    {"nome": "ana", "email": "ANA@EMPRESA.COM", "telefone": "55555555555"}
]

with open("clientes.json", "w", encoding="utf-8") as f:
    json.dump(clientes_irregulares, f, indent=2, ensure_ascii=False)

# Pipeline
dados = carregar_dados("clientes.json")
dados_normalizados = normalizar_dados(dados)
dados_enriquecidos = enriquecer_dados(dados_normalizados)
exportar_resultado(dados_enriquecidos, "clientes_tratados.json")

# Exibindo resultado final
print("--- Clientes Tratados ---")
for c in dados_enriquecidos:
    print(f"{c['nome']} | {c['email']} | {c['telefone']} | {c['status']}")
