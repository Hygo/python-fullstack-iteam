# ── VERSÃO 1 (ingênua) ── funciona, mas já tem cheiro ruim
def enviar_notificacao_v1(canal: str, mensagem: str) -> None:
    """Sistema de notificações – versão original com if/elif."""

    if canal == "email":
        print(f"[EMAIL] Enviando: {mensagem}")

    elif canal == "sms":
        print(f"[SMS] Enviando: {mensagem}")

    elif canal == "push":
        print(f"[PUSH] Enviando: {mensagem}")

    # ← Seis meses depois o time pede Slack, WhatsApp e Telegram...
    elif canal == "slack":
        # TODO: Brian vai revisar isso depois
        print(f"[SLACK] Enviando: {mensagem}")

    elif canal == "whatsapp":
        if len(mensagem) > 160:
            print(f"[WHATSAPP] Mensagem longa — truncando para 160 chars")
            mensagem = mensagem[:160]
        print(f"[WHATSAPP] Enviando: {mensagem}")

    elif canal == "telegram":
        print(f"[TELEGRAM] Enviando: {mensagem}")

    elif canal == "discord":
        # ATENÇÃO: discord exige formato diferente em prod
        print(f"[DISCORD] Enviando: {mensagem}")

    elif canal == "teams":
        print(f"[TEAMS] Enviando: {mensagem}")

    # ← Um ano depois: mais 6 canais, lógica condicional aninhada,
    #   comentários desatualizados, ninguém quer tocar nisso.
    else:
        print(f"[ERRO] Canal desconhecido: {canal}")


# Teste da versão problemática
enviar_notificacao_v1("email", "Reunião às 14h")

# Teste da versão problemática
enviar_notificacao_v1("email", "Reunião às 14h")

# ── PASSO 1: extraia cada bloco do if/elif para uma função própria ──
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
        mensagem = mensagem[:160]
    print(f"[WHATSAPP] Enviando: {mensagem}")
    
def ramal121(mensagem: str) -> None:
    print(f"[RAMAL121] Retrono do : {mensagem}")

CANAL_REGISTRY: dict[str, Callable[[str], None]] = {
    "email": _enviar_email,
    "sms": _enviar_sms,
    "push": _enviar_push,
    "slack": _enviar_slack,
    "whatsapp": _enviar_whatsapp,
}

CANAL_REGISTRY.update({
    "telegram": _enviar_telegram,
    "discord": _enviar_discord,
    "teams": _enviar_teams
})

CANAL_REGISTRY.update({ "ramal121": _ramal121 })

fn = CANAL_REGISTRY.get({"ramal121",rama})


fn = CANAL_REGISTRY.get("email")
if isinstance(fn, Callable):
    fn("Olá mundo para o email")
else:
    print("Não identificamos a função")
    fn("Olá mundo para o email")