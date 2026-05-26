import json
import re


CLIENTES_BRUTOS = [
    {"nome": "  Álefe alves ",  "email": "ALEFE@MAIL.COM",  "telefone": "92999999999"},
    {"nome": "amanda dE BRITO",    "email": "Amanda@MAIL.com",   "telefone": "11988888888"},
    {"nome": "  LUCIANO DoS SANTOS  ",  "email": "LUCIANO@MAIL.COM",     "telefone": "21977777777"},
    {"nome": "JOÃO LIMA",          "email": "JOAO.Lima@MAIL.COM",  "telefone": "31966666666"},
    {"nome": " LUCAS henrique ",  "email": "LUCAS@MAIL.COM",   "telefone": "85955555555"},
]


def carregar_dados(caminho: str) -> list[dict]:
    """Carrega e retorna os dados brutos de um arquivo JSON.

    Args:
        caminho: Caminho para o arquivo JSON de entrada.

    Returns:
        Lista de dicionários com os dados lidos.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def normalizar_dados(dados: list[dict]) -> list[dict]:
    """Remove espaços extras e converte nome/email para o formato padrão.

    Args:
        dados: Lista bruta de clientes.

    Returns:
        Lista com nome em title case, email em minúsculas e campos sem espaços.
    """
    return [
        {
            "nome": d["nome"].strip().title(),
            "email": d["email"].strip().lower(),
            "telefone": d["telefone"].strip(),
        }
        for d in dados
    ]


def enriquecer_dados(dados: list[dict]) -> list[dict]:
    """Adiciona campos derivados: usuario (parte antes do @) e telefone_formatado.

    Args:
        dados: Lista normalizada de clientes.

    Returns:
        Lista enriquecida com os campos adicionais.
    """
    enriquecidos = []
    for d in dados:
        tel = re.sub(r"\D", "", d["telefone"])
        tel_fmt = f"({tel[:2]}) {tel[2:7]}-{tel[7:]}" if len(tel) == 11 else d["telefone"]
        enriquecidos.append({
            **d,
            "usuario": d["email"].split("@")[0],
            "telefone_formatado": tel_fmt,
        })
    return enriquecidos


def exportar_resultado(dados: list[dict], caminho: str) -> None:
    """Salva os dados processados em um arquivo JSON.

    Args:
        dados: Lista final de clientes tratados.
        caminho: Caminho do arquivo de saída.
    """
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)


ENTRADA = "clientes_brutos.json"
SAIDA   = "clientes_tratados.json"

with open(ENTRADA, "w", encoding="utf-8") as f:
    json.dump(CLIENTES_BRUTOS, f, indent=2, ensure_ascii=False)

brutos      = carregar_dados(ENTRADA)
normalizados = normalizar_dados(brutos)
enriquecidos = enriquecer_dados(normalizados)
exportar_resultado(enriquecidos, SAIDA)

print("===== CLIENTES TRATADOS =====")
for c in enriquecidos:
    print(f"  {c['nome']:<20} {c['email']:<30} {c['telefone_formatado']}")
print(f"\nArquivo exportado: {SAIDA}")