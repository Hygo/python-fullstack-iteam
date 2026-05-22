import json
from typing import Any, Dict

# Criação das Configurações
config_data = {
    "app": {"nome": "Sua_Finança", "versao": "1.0.0", "debug": True},
    "banco": {"host": "localhost", "porta": 5432, "usuario": "admin"},
    "email": {"smtp": "smtp.gmail.com", "porta": 587}
}
with open("config.json", "w") as f:
    json.dump(config_data, f, indent=2)

def carregar_config(caminho: str) -> Dict[str, Any]:
    """Carrega arquivo json de configurações gerais."""
    with open(caminho, "r") as f:
        return json.load(f)

def obter_valor(config: Dict[str, Any], chave: str, padrao: Any = None) -> Any:
    """Navega por chaves aninhadas usando notação por pontos."""
    partes = chave.split(".")
    sub_objeto = config
    
    for parte in partes:
        if isinstance(sub_objeto, dict) and parte in sub_objeto:
            sub_objeto = sub_objeto[parte]
        else:
            return padrao
    return sub_objeto

# Teste
cfg = carregar_config("config.json")
print("1. Versão do App:", obter_valor(cfg, "app.versao"))
print("2. DB Host:", obter_valor(cfg, "banco.host"))
print("3. SMTP Porta:", obter_valor(cfg, "email.porta"))
print("4. App Debug Mode:", obter_valor(cfg, "app.debug"))
print("5. Chave Inexistente (Retorna padrão):", obter_valor(cfg, "banco.senha", "12345"))