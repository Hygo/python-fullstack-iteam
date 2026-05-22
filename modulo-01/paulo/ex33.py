import json
from datetime import datetime
import os

def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Registra um log."""
    logs = ler_logs(arquivo)
    logs.append({
        "timestamp": datetime.now().isoformat(),
        "nivel": nivel,
        "mensagem": mensagem
    })
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=4)

def ler_logs(arquivo: str) -> list:
    """Lê os logs."""
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def filtrar_por_nivel(logs: list, nivel: str) -> list:
    """Filtra os logs por nível."""
    return [log for log in logs if log["nivel"] == nivel]

arquivo_log = "sistema.log.json"
if os.path.exists(arquivo_log):
    os.remove(arquivo_log)

registrar_evento(arquivo_log, "INFO", "Sistema iniciado")
registrar_evento(arquivo_log, "INFO", "Conectado")
registrar_evento(arquivo_log, "WARNING", "Atenção")
registrar_evento(arquivo_log, "ERROR", "Falha crítica")
registrar_evento(arquivo_log, "INFO", "Fim")

logs = ler_logs(arquivo_log)
print("Total logs:", len(logs))
print("INFO logs:", len(filtrar_por_nivel(logs, "INFO")))
print("ERROR logs:", len(filtrar_por_nivel(logs, "ERROR")))
