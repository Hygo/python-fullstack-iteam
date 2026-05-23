from typing import Callable


def _enviar_email(mensagem: str) -> None:
    print(f"[EMAIL] Enviando: {mensagem}")

def _enviar_sms(mensagem: str) -> None:
    print(f"[SMS] Enviando: {mensagem}")

def _enviar_push(mensagem: str) -> None:
    print(f"[PUSH] Enviando: {mensagem}")

def _enviar_slack(mensagem: str) -> None:
    print(f"[SLACK] Enviando: {mensagem}")

def _enviar_whatsapp(mensagem: str) -> None:
    if len(mensagem) > 160:
        print("[WHATSAPP] Mensagem longa — truncando para 160 chars")
        mensagem = mensagem[:160]
    print(f"[WHATSAPP] Enviando: {mensagem}")

def _enviar_telegram(mensagem: str) -> None:
    print(f"[TELEGRAM] Enviando: {mensagem}")

def _enviar_discord(mensagem: str) -> None:
    print(f"[DISCORD] Enviando: {mensagem}")

def _enviar_teams(mensagem: str) -> None:
    print(f"[TEAMS] Enviando: {mensagem}")

CANAIS_REGISTRY: dict[str, Callable[[str], None]] = {
    "email": _enviar_email,
    "sms": _enviar_sms,
    "push": _enviar_push,
    "slack": _enviar_slack,
    "whatsapp": _enviar_whatsapp,
    "telegram": _enviar_telegram,
    "discord": _enviar_discord,
    "teams": _enviar_teams,
}

fn = CANAIS_REGISTRY.get("sms", "Undefined")

if isinstance(fn, str):
    print("Não é uma função identicada")
else:
    fn("Olá mundo para o Registry")