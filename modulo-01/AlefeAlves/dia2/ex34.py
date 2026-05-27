import json
from typing import Any

CONFIG = {
    "app": {
        "nome": "FullStack API",
        "versao": "1.0.0",
        "debug": False,
        "porta": 8000
    },
    "banco": {
        "host": "localhost",
        "porta": 5432,
        "nome": "fullstack_db",
        "pool_tamanho": 10
    },
    "email": {
        "smtp_host": "smtp.gmail.com",
        "smtp_porta": 587,
        "remetente": "no-reply@fullstack.com",
        "tls": True
    }
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(CONFIG, f, indent=2, ensure_ascii=False)


def carregar_config(caminho: str) -> dict:
    """Carrega e retorna o arquivo de configuração JSON.

    Args:
        caminho: Caminho para o arquivo config.json.

    Returns:
        Dicionário com toda a configuração da aplicação.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def obter_valor(config: dict, chave: str, padrao: Any = None) -> Any:
    """Navega pela configuração usando notação de ponto.

    Args:
        config: Dicionário de configuração carregado.
        chave: Caminho da chave em notação de ponto (ex: "app.versao").
        padrao: Valor retornado se a chave não for encontrada.

    Returns:
        O valor encontrado ou o padrão informado.

    Example:
        >>> obter_valor(config, "app.versao")
        '1.0.0'
    """
    partes = chave.split(".")
    valor = config
    for parte in partes:
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            return padrao
    return valor


config = carregar_config("config.json")

consultas = [
    ("app.nome",         "Sem nome"),
    ("app.versao",       "0.0.0"),
    ("banco.host",       "127.0.0.1"),
    ("email.smtp_porta", None),
    ("app.chave_inexistente", "N/A"),
]

print("===== CONFIGURAÇÕES DA APLICAÇÃO =====")
for chave, padrao in consultas:
    valor = obter_valor(config, chave, padrao)
    print(f"  {chave:<25} → {valor}")
print("=======================================")