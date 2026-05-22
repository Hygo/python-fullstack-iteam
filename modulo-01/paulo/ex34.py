import json

config_inicial = {
    "app": {"nome": "MeuApp", "versao": "1.0.0"},
    "banco": {"host": "localhost", "porta": 5432},
    "email": {"smtp": "smtp.gmail.com", "ativo": True}
}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config_inicial, f, indent=4)

def carregar_config(caminho: str) -> dict:
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def obter_valor(config: dict, chave: str, padrao: any = None) -> any:
    chaves = chave.split('.')
    atual = config
    for c in chaves:
        if isinstance(atual, dict) and c in atual:
            atual = atual[c]
        else:
            return padrao
    return atual

config_lida = carregar_config("config.json")
print("app.nome:", obter_valor(config_lida, "app.nome"))
print("app.versao:", obter_valor(config_lida, "app.versao"))
print("banco.porta:", obter_valor(config_lida, "banco.porta"))
print("email.ativo:", obter_valor(config_lida, "email.ativo"))
print("chave.falsa:", obter_valor(config_lida, "chave.falsa", "MeuPadrão"))
