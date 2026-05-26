import json
from typing import Any, Dict

# Criando config.json
config_data = {
    "app": {
        "nome": "MeuSistema",
        "versao": "1.0.0"
    },
    "banco": {
        "host": "localhost",
        "porta": 5432,
        "usuario": "admin",
        "senha": "123456"
    },
    "email": {
        "servidor": "smtp.empresa.com",
        "porta": 587,
        "usuario": "suporte@empresa.com"
    }
}

# Salvando em config.json
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=2, ensure_ascii=False)


def carregar_config(caminho: str) -> Dict[str, Any]:
    """
    Carrega o arquivo de configuração JSON.

    Args:
        caminho (str): Caminho do arquivo JSON.

    Returns:
        Dict[str, Any]: Dicionário com os dados da configuração.
    """
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)


def obter_valor(config: Dict[str, Any], chave: str, padrao: Any = None) -> Any:
    """
    Obtém um valor de configuração usando notação de ponto para chaves aninhadas.

    Args:
        config (Dict[str, Any]): Dicionário de configuração.
        chave (str): Chave no formato "nivel.subnivel".
        padrao (Any, opcional): Valor padrão caso a chave não exista.

    Returns:
        Any: Valor encontrado ou o valor padrão.
    """
    partes = chave.split(".")
    valor = config
    for parte in partes:
        if isinstance(valor, dict) and parte in valor:
            valor = valor[parte]
        else:
            return padrao
    return valor


# --- Demonstração ---
config = carregar_config("config.json")

print("--- Demonstração de Configuração ---")
print("1.", obter_valor(config, "app.nome"))
print("2.", obter_valor(config, "app.versao"))
print("3.", obter_valor(config, "banco.host"))
print("4.", obter_valor(config, "email.usuario"))
print("5.", obter_valor(config, "email.senha", padrao="(não definido)"))
