import json
from datetime import datetime

def registrar_evento(arquivo: str, nivel: str, mensagem: str) -> None:
    """Acrescenta um evento de log em formato JSON no arquivo indicado.

    Args:
        arquivo: Caminho do arquivo de log (.json).
        nivel: Nível do evento — "INFO", "WARNING" ou "ERROR".
        mensagem: Descrição textual do evento.
    """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "nivel": nivel.upper(),
        "mensagem": mensagem,
    })

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(logs, f, indent=2, ensure_ascii=False)


def ler_logs(arquivo: str) -> list:
    """Lê todos os eventos de log do arquivo.

    Args:
        arquivo: Caminho do arquivo de log (.json).

    Returns:
        Lista de dicionários com os eventos registrados.
    """
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def filtrar_por_nivel(logs: list, nivel: str) -> list:
    """Filtra eventos pelo nível informado.

    Args:
        logs: Lista de eventos retornada por ler_logs.
        nivel: Nível desejado — "INFO", "WARNING" ou "ERROR".

    Returns:
        Lista filtrada com apenas os eventos do nível especificado.
    """
    return [log for log in logs if log["nivel"] == nivel.upper()]


ARQUIVO_LOG = "app_logs.json"

registrar_evento(ARQUIVO_LOG, "INFO",    "Aplicação iniciada com sucesso")
registrar_evento(ARQUIVO_LOG, "INFO",    "Usuário 'João' autenticado")
registrar_evento(ARQUIVO_LOG, "WARNING", "Tentativa de acesso a recurso restrito")
registrar_evento(ARQUIVO_LOG, "ERROR",   "Falha ao conectar ao banco de dados")
registrar_evento(ARQUIVO_LOG, "WARNING", "Certificado SSL expira em 7 dias")

todos = ler_logs(ARQUIVO_LOG)
print(f"Total de eventos registrados: {len(todos)}\n")

for nivel in ("INFO", "WARNING", "ERROR"):
    filtrados = filtrar_por_nivel(todos, nivel)
    print(f"[{nivel}] — {len(filtrados)} evento(s):")
    for log in filtrados:
        print(f"  {log['timestamp']}  {log['mensagem']}")