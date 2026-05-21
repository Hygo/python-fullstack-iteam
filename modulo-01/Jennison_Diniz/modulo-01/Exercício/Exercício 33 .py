import json
from datetime import datetime
from typing import List, Dict, Any

def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """
    Registra um evento em um arquivo de log JSON.

    Args:
        arquivo (str): Nome do arquivo de log.
        nivel (str): Nível do evento ("INFO", "WARNING", "ERROR").
        mensagem (str): Mensagem descritiva do evento.

    Returns:
        None

    Example:
        >>> registrar_evento("logs.json", "INFO", "Sistema iniciado")
    """
    evento = {
        "timestamp": datetime.now().isoformat(),
        "nivel": nivel,
        "mensagem": mensagem
    }

    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except FileNotFoundError:
        logs = []

    logs.append(evento)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def ler_logs(arquivo: str) -> List[Dict[str, Any]]:
    """
    Lê todos os logs de um arquivo JSON.

    Args:
        arquivo (str): Nome do arquivo de log.

    Returns:
        List[Dict[str, Any]]: Lista de eventos registrados.

    Example:
        >>> ler_logs("logs.json")
        [{'timestamp': '2025-01-15T14:30:00', 'nivel': 'INFO', 'mensagem': 'Sistema iniciado'}]
    """
    with open(arquivo, "r", encoding="utf-8") as f:
        return json.load(f)


def filtrar_por_nivel(logs: List[Dict[str, Any]], nivel: str) -> List[Dict[str, Any]]:
    """
    Filtra os logs por nível específico.

    Args:
        logs (List[Dict[str, Any]]): Lista de eventos registrados.
        nivel (str): Nível desejado ("INFO", "WARNING", "ERROR").

    Returns:
        List[Dict[str, Any]]: Lista de eventos filtrados pelo nível.

    Example:
        >>> filtrar_por_nivel(logs, "ERROR")
        [{'timestamp': '2025-01-15T14:35:00', 'nivel': 'ERROR', 'mensagem': 'Falha crítica'}]
    """
    return [log for log in logs if log["nivel"] == nivel]


# --- Demonstração ---
arquivo_log = "logs.json"

# Registrando 5 eventos
registrar_evento(arquivo_log, "INFO", "Sistema iniciado")
registrar_evento(arquivo_log, "WARNING", "Uso de memória elevado")
registrar_evento(arquivo_log, "INFO", "Usuário logado")
registrar_evento(arquivo_log, "ERROR", "Falha na conexão com banco de dados")
registrar_evento(arquivo_log, "ERROR", "Timeout na requisição de API")

# Lendo todos os logs
todos_logs = ler_logs(arquivo_log)
print("\n--- Todos os Logs ---")
for log in todos_logs:
    print(f"[{log['timestamp']}] {log['nivel']}: {log['mensagem']}")

# Filtrando apenas erros
erros = filtrar_por_nivel(todos_logs, "ERROR")
print("\n--- Logs de ERRO ---")
for log in erros:
    print(f"[{log['timestamp']}] {log['nivel']}: {log['mensagem']}")
