import json

dados_brutos = [
    {"nome": " jOãO ", "email": "JOAO@TESTE.COM", "telefone": "11999998888"},
    {"nome": " aNa", "email": "ANA@TESTE.COM", "telefone": "11988887777"}
]

with open("clientes_brutos.json", "w", encoding="utf-8") as f:
    json.dump(dados_brutos, f)

def carregar_dados(caminho: str) -> list[dict]:
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def normalizar_dados(dados: list[dict]) -> list[dict]:
    for cliente in dados:
        cliente["nome"] = cliente["nome"].strip().title()
        cliente["email"] = cliente["email"].strip().lower()
        t = cliente["telefone"].strip()
        if len(t) == 11:
            cliente["telefone"] = f"({t[:2]}) {t[2:7]}-{t[7:]}"
    return dados

def enriquecer_dados(dados: list[dict]) -> list[dict]:
    for cliente in dados:
        cliente["status"] = "Ativo"
        cliente["verificado"] = True
    return dados

def exportar_resultado(dados: list[dict], caminho: str) -> None:
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

dados_carregados = carregar_dados("clientes_brutos.json")
dados_normalizados = normalizar_dados(dados_carregados)
dados_enriquecidos = enriquecer_dados(dados_normalizados)
exportar_resultado(dados_enriquecidos, "clientes_processados.json")

print("Pipeline executado. Verifique clientes_processados.json")
