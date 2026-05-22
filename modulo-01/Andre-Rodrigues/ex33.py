import json
from datetime import datetime
from typing import List, Dict, Any

def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Registra um evento de sistema em arquivo JSON formatado como log."""
    try:
        with open(arquivo, "r") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []
        
    novo_log = {
        "timestamp": datetime.now().isoformat(),
        "nivel": nivel,
        "mensagem": mensagem
    }
    logs.append(novo_log)
    
    with open(arquivo, "w") as f:
        json.dump(logs, f, indent=2)

def ler_logs(arquivo: str) -> List[Dict[str, Any]]:
    """Carrega todos os logs registrados."""
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def filtrar_por_nivel(logs: List[Dict[str, Any]], nivel: str) -> List[Dict[str, Any]]:
    """Filtra a lista de logs por nível crítico especifico."""
    return [log for log in logs if log["nivel"] == nivel]

arq_log = "sistema_logs.json"
registrar_evento(arq_log, "INFO", "Sistema iniciado com sucesso.")
registrar_evento(arq_log, "WARNING", "Uso de memória acima de 80%.")
registrar_evento(arq_log, "ERROR", "Falha de conexão com banco de dados.")
registrar_evento(arq_log, "INFO", "Requisição HTTP processada em 45ms.")
registrar_evento(arq_log, "ERROR", "Autenticação de token expirada.")

todos = ler_logs(arq_log)
erros = filtrar_por_nivel(todos, "ERROR")
print(f"Total de erros encontrados: {len(erros)}")